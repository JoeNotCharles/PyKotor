from xml.etree.ElementTree import ParseError

from pykotor.common.stream import BinaryReader
from pykotor.resource.formats.gff import GFF, GFFBinaryReader, GFFBinaryWriter, GFFContent, GFFXMLWriter, GFFXMLReader
from pykotor.resource.type import SOURCE_TYPES, TARGET_TYPES, ResourceType


def detect_gff(
        source: SOURCE_TYPES,
        offset: int = 0
) -> ResourceType:
    """
    Returns what format the GFF data is believed to be in. This function performs a basic check and does not guarantee
    accuracy of the result or integrity of the data.

    Args:
        source: Source of the GFF data.
        offset: Offset into the data.

    Raises:
        FileNotFoundError: If the file could not be found.
        IsADirectoryError: If the specified path is a directory (Unix-like systems only).
        PermissionError: If the file could not be accessed.

    Returns:
        The format of the GFF data.
    """
    try:
        if isinstance(source, str):
            with BinaryReader.from_file(source, offset) as reader:
                file_header = reader.read_string(4)
                file_format = ResourceType.GFF if any(
                    x.value == file_header for x in GFFContent) else ResourceType.GFF_XML
        elif isinstance(source, bytes) or isinstance(source, bytearray):
            file_format = ResourceType.GFF if any(
                x for x in GFFContent if x.value == source[:4].decode('ascii', 'ignore')) else ResourceType.GFF_XML
        elif isinstance(source, BinaryReader):
            file_header = source.read_string(4)
            file_format = ResourceType.GFF if any(x.value == file_header for x in GFFContent) else ResourceType.GFF_XML
            source.skip(-4)
        else:
            file_format = ResourceType.INVALID
    except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
        raise e
    except IOError:
        file_format = ResourceType.INVALID

    return file_format


def read_gff(
        source: SOURCE_TYPES,
        offset: int = 0,
        size: int = None
) -> GFF:
    """
    Returns an GFF instance from the source. The file format (GFF or GFF_XML) is automatically determined before parsing
    the data.

    Args:
        source: The source of the data.
        offset: The byte offset of the file inside the data.
        size: Number of bytes to allowed to read from the stream. If not specified, uses the whole stream.

    Raises:
        FileNotFoundError: If the file could not be found.
        IsADirectoryError: If the specified path is a directory (Unix-like systems only).
        PermissionError: If the file could not be accessed.
        ValueError: If the file was corrupted or the format could not be determined.

    Returns:
        A GFF instance.
    """
    file_format = detect_gff(source, offset)

    if file_format is ResourceType.INVALID:
        raise ValueError("Failed to determine the format of the GFF file.")

    if file_format == ResourceType.GFF:
        return GFFBinaryReader(source, offset, size).load()
    elif file_format == ResourceType.GFF_XML:
        return GFFXMLReader(source, offset, size).load()


def write_gff(
        gff: GFF,
        target: TARGET_TYPES,
        file_format: ResourceType = ResourceType.GFF
) -> None:
    """
    Writes the GFF data to the target location with the specified format (GFF or GFF_XML).

    Args:
        gff: The GFF file being written.
        target: The location to write the data to.
        file_format: The file format.

    Raises:
        IsADirectoryError: If the specified path is a directory (Unix-like systems only).
        PermissionError: If the file could not be written to the specified destination.
        ValueError: If the specified format was unsupported.
    """
    if file_format == ResourceType.GFF:
        GFFBinaryWriter(gff, target).write()
    elif file_format == ResourceType.GFF_XML:
        GFFXMLWriter(gff, target).write()
    else:
        raise ValueError("Unsupported format specified; use GFF or GFF_XML.")


def bytes_gff(
        gff: GFF,
        file_format: ResourceType = ResourceType.GFF
) -> bytes:
    """
    Returns the GFF data in the specified format (GFF or GFF_XML) as a bytes object.

    This is a convience method that wraps the write_gff() method.

    Args:
        gff: The target GFF object.
        file_format: The file format.

    Raises:
        ValueError: If the specified format was unsupported.

    Returns:
        The GFF data.
    """
    data = bytearray()
    write_gff(gff, data, file_format)
    return data
