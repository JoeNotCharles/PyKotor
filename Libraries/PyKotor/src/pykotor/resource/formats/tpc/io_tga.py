from __future__ import annotations

import struct
from enum import IntEnum

from pykotor.common.stream import BinaryReader
from pykotor.resource.formats.tpc.tpc_data import TPC, TPCTextureFormat
from pykotor.resource.type import SOURCE_TYPES, TARGET_TYPES, ResourceReader, ResourceWriter, autoclose


class _DataTypes(IntEnum):
    NO_IMAGE_DATA = 0
    UNCOMPRESSED_COLOR_MAPPED = 1
    UNCOMPRESSED_RGB = 2
    UNCOMPRESSED_BLACK_WHITE = 3
    RLE_COLOR_MAPPED = 9
    RLE_RGB = 10
    COMPRESSED_BLACK_WHITE = 11
    COMPRESSED_COLOR_MAPPED_A = 32
    COMPRESSED_COLOR_MAPPED_B = 33

class TPCTGAReader(ResourceReader):
    def __init__(
        self,
        source: SOURCE_TYPES,
        offset: int = 0,
        size: int = 0,
    ):
        super().__init__(source, offset, size)
        self._tpc: TPC | None = None

    def _read_color_map(self, length, depth) -> list[bytes]:
        color_map: list[bytes] = []
        bytes_per_entry = depth // 8

        for _ in range(length):
            entry: bytes = self._reader.read_bytes(bytes_per_entry)
            if bytes_per_entry == 3:  # RGB format, append alpha value
                entry += b"\xff"  # Append alpha value of 255
            color_map.append(entry)

        return color_map

    def _convert_grayscale_to_rgba(self, grayscale_value: int) -> list[int]:
        """Convert a grayscale value to RGBA."""
        return [grayscale_value, grayscale_value, grayscale_value, 255]

    def _process_rle_data(
        self,
        width: int,
        height: int,
        bits_per_pixel: int,
        color_map: list[bytes] | None = None,
        is_direct_rgb: bool = False,  # New parameter
    ) -> bytearray:
        """Process RLE compressed data."""
        data = bytearray()
        n = 0
        pixel: list[int]
        rgb_len = 3
        while self._reader.remaining():  # while n < width * height:
            packet = self._reader.read_uint8()
            count = (packet & 0b01111111) + 1
            is_raw_packet: bool = (packet >> 7) == 0
            #count = (packet & 0x7f) + 1
            #is_raw_packet = packet & 0x80
            n += count

            if is_raw_packet:
                for _ in range(count):
                    if is_direct_rgb:
                        b, g, r = (
                            self._reader.read_uint8(),
                            self._reader.read_uint8(),
                            self._reader.read_uint8(),
                        )
                        pixel = [r, g, b, self._reader.read_uint8()] if bits_per_pixel == 32 else [r, g, b, 255]
                    elif color_map:
                        index = self._reader.read_uint8()
                        color = list(color_map[index])
                        if len(color) == rgb_len:  # Check the length of the color map entry
                            color.append(255)  # Append alpha value 255
                        pixel = color
                    else:
                        pixel = self._convert_grayscale_to_rgba(self._reader.read_uint8())

                    data.extend(pixel)
            else:
                if is_direct_rgb:
                    b, g, r = (
                        self._reader.read_uint8(),
                        self._reader.read_uint8(),
                        self._reader.read_uint8(),
                    )
                    pixel = [r, g, b, self._reader.read_uint8()] if bits_per_pixel == 32 else [r, g, b, 255]
                elif color_map:
                    index = self._reader.read_uint8()
                    color = list(color_map[index])
                    if len(color) == rgb_len:  # Check the length of the color map entry
                        color.append(255)  # Append alpha value 255
                    pixel = color
                else:
                    pixel = self._convert_grayscale_to_rgba(self._reader.read_uint8())
                for _ in range(count):
                    data.extend(pixel)
            if n == width * height:
                break
        return data


    def _process_non_rle_color_mapped(self, width: int, height: int, color_map: list[bytes]) -> bytearray:
        """Process non-RLE color-mapped data."""
        data = bytearray()
        for _ in range(width * height):
            index = self._reader.read_uint8()
            data.extend(color_map[index])
        return data

    @autoclose
    def load(
        self,
        auto_close: bool = True,
    ) -> TPC:
        """Loads image data from the reader into a TPC texture.

        Args:
        ----
            self: The loader object
            auto_close: Whether to close the reader after loading

        Returns:
        -------
            TPC: The loaded TPC texture

        Processing Logic:
        ----------------
            - Read header values from the reader
            - Check for uncompressed or RLE encoded RGB data
            - Load pixel data into rows or run lengths
            - Assemble pixel data into a single bytearray
            - Set the loaded data on the TPC texture.
        """
        self._tpc = TPC()

        id_length = self._reader.read_uint8()
        colormap_type = self._reader.read_uint8()
        datatype_code = self._reader.read_uint8()
        colormap_origin = self._reader.read_uint16()  # noqa: F841
        colormap_length = self._reader.read_uint16()
        colormap_depth = self._reader.read_uint8()
        x_origin = self._reader.read_uint16()  # noqa: F841
        y_origin = self._reader.read_uint16()  # noqa: F841
        width = self._reader.read_uint16()
        height = self._reader.read_uint16()
        bits_per_pixel = self._reader.read_uint8()
        image_descriptor = self._reader.read_uint8()
        self._reader.skip(id_length)

        # Read the color map if necessary
        color_map = None
        if colormap_type and colormap_length:
            color_map = self._read_color_map(colormap_length, colormap_depth)

        y_flipped = bool(image_descriptor & 0b00100000)
        interleaving_id = (image_descriptor & 0b11000000) >> 6
        if interleaving_id:
            ValueError("The image data must not be interleaved.")

        data: bytearray = bytearray()
        if datatype_code == _DataTypes.UNCOMPRESSED_COLOR_MAPPED:
            if color_map is None:
                msg = "Expected color map not found for uncompressed color-mapped data"
                raise ValueError(msg)
            data = self._process_non_rle_color_mapped(width, height, color_map)
        elif datatype_code == _DataTypes.UNCOMPRESSED_RGB:
            self._reader.skip(colormap_length * colormap_depth // 8)

            if bits_per_pixel not in {24, 32}:
                ValueError("The image must store 24 or 32 bits per pixel.")

            pixel_rows: list[bytearray] = []
            for y in range(height):
                pixel_rows.append(bytearray())
                for _ in range(width):
                    b, g, r = (
                        self._reader.read_uint8(),
                        self._reader.read_uint8(),
                        self._reader.read_uint8(),
                    )
                    if bits_per_pixel == 32:
                        pixel_rows[y].extend([r, g, b, self._reader.read_uint8()])
                    else:
                        pixel_rows[y].extend([r, g, b])

            if y_flipped:
                for pixels in reversed(pixel_rows):
                    data.extend(pixels)
            else:
                for pixels in pixel_rows:
                    data.extend(pixels)
        elif datatype_code == _DataTypes.UNCOMPRESSED_BLACK_WHITE:
            data = bytearray()
            for _ in range(width * height):
                # Read the grayscale value (assuming 1 byte per pixel)
                gray_value = self._reader.read_uint8()

                # Convert grayscale to RGBA (R=G=B=gray_value, A=255)
                data.extend([gray_value, gray_value, gray_value, 255])
        elif datatype_code == _DataTypes.RLE_COLOR_MAPPED:
            if color_map is None:
                msg = "Expected color map not found for RLE color-mapped data"
                raise ValueError(msg)
            data = self._process_rle_data(width, height, bits_per_pixel, color_map=color_map)
        elif datatype_code == _DataTypes.RLE_RGB:
            data = self._process_rle_data(width, height, bits_per_pixel, is_direct_rgb=True)
        elif datatype_code == _DataTypes.COMPRESSED_BLACK_WHITE:
            data = self._process_rle_data(width, height, bits_per_pixel)
        elif datatype_code in {_DataTypes.COMPRESSED_COLOR_MAPPED_A, _DataTypes.COMPRESSED_COLOR_MAPPED_B}:
            if color_map is None:
                msg = "Expected color map not found for compressed color-mapped data"
                raise ValueError(msg)
            data = self._process_rle_data(width, height, bits_per_pixel, color_map=color_map)
        else:
            msg = "The image format is not currently supported."
            raise ValueError(msg)

        self._tpc.set_data(width, height, [bytes(data)], TPCTextureFormat.RGBA)

        return self._tpc


class TPCTGAWriter(ResourceWriter):
    def __init__(
        self,
        tpc: TPC,
        target: TARGET_TYPES,
    ):
        super().__init__(target)
        self._tpc: TPC = tpc

    @autoclose
    def write(
        self,
        auto_close: bool = True,
    ):
        """Writes the TPC texture to a BMP file.

        Args:
        ----
            self: The TPCWriter instance
            auto_close: Whether to close the underlying file stream (default True).

        Processing Logic:
        ----------------
            - Get width and height of texture from TPC instance
            - Write BMP file header
            - Write pixel data in RGB or RGBA format depending on TPC format.
        """
        width, height = self._tpc.dimensions()

        self._writer.write_uint8(0)  # id length
        self._writer.write_uint8(0)  # colormap_type
        self._writer.write_uint8(2)  # datatype_code
        self._writer.write_bytes(bytes(5))  # colormap_origin
        self._writer.write_uint16(0)  # colormap_length, colormap_depth
        self._writer.write_uint16(0)  # x,y origin
        self._writer.write_uint16(width)
        self._writer.write_uint16(height)

        if self._tpc.format() in [TPCTextureFormat.RGB or TPCTextureFormat.DXT1]:
            self._writer.write_uint8(32)  # bits_per_pixel, image_descriptor
            self._writer.write_uint8(0)
            data: bytes | None = self._tpc.convert(TPCTextureFormat.RGB, 0).data
            pixel_reader: BinaryReader = BinaryReader.from_bytes(data)
            for _ in range(len(data) // 3):
                r = pixel_reader.read_uint8()
                g = pixel_reader.read_uint8()
                b = pixel_reader.read_uint8()
                self._writer.write_bytes(struct.pack("BBBB", b, g, r, 255))
        else:
            self._writer.write_uint8(32)
            self._writer.write_uint8(0)
            width, height, data = self._tpc.convert(TPCTextureFormat.RGBA, 0)
            pixel_reader = BinaryReader.from_bytes(data)
            for _ in range(len(data) // 4):
                r = pixel_reader.read_uint8()
                g = pixel_reader.read_uint8()
                b = pixel_reader.read_uint8()
                a = pixel_reader.read_uint8()
                self._writer.write_bytes(struct.pack("BBBB", b, g, r, a))