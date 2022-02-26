from typing import Union

from pykotor.resource.type import ResourceType

from pykotor.common.stream import BinaryReader
from pykotor.resource.formats.vis import VIS, VISAsciiWriter, VISAsciiReader


def load_vis(source: Union[str, bytes, bytearray, BinaryReader], offset: int = 0, size: int = None) -> VIS:
    """
    Returns an VIS instance from the source. The file format (VIS only) is automatically determined before parsing
    the data.

    Args:
        source: The source of the data.
        offset: The byte offset of the file inside the data.
        size: Number of bytes to allowed to read from the stream. If not specified, uses the whole stream.

    Raises:
        ValueError: If the file was corrupted or in an unsupported format.

    Returns:
        An VIS instance.
    """
    try:
        return VISAsciiReader(source, offset, size).load()
    except IOError:
        raise ValueError("Tried to load an unsupported or corrupted VIS file.")


def write_vis(vis: VIS, target: Union[str, bytearray, BinaryReader], file_format: ResourceType = ResourceType.VIS) -> None:
    """
    Writes the VIS data to the target location with the specified format (VIS only).

    Args:
        vis: The VIS file being written.
        target: The location to write the data to.
        file_format: The file format.

    Raises:
        ValueError: If an unsupported file format was given.
    """
    if file_format == ResourceType.VIS:
        VISAsciiWriter(vis, target).write()
    else:
        raise ValueError("Unsupported format specified; use VIS.")
