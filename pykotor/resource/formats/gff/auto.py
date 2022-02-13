from pykotor.common.stream import BinaryReader
from pykotor.resource.formats.gff import GFF, GFFBinaryReader, GFFBinaryWriter, GFFContent, GFFXMLWriter, GFFXMLReader
from pykotor.resource.type import SOURCE_TYPES, TARGET_TYPES, ResourceType


def detect_gff(source: SOURCE_TYPES, offset: int = 0) -> ResourceType:
    """
    Returns what format the GFF data is believed to be in. This function performs a basic check and does not guarantee
    accuracy of the result or integrity of the data.

    Args:
        source: Source of the GFF data.
        offset: Offset into the data.

    Returns:
        The format of the GFF data.
    """
    try:
        if isinstance(source, str):
            with BinaryReader.from_file(source, offset) as reader:
                file_header = reader.read_string(4)
                file_format = ResourceType.GFF if any(x.value == file_header for x in GFFContent) else ResourceType.GFF_XML
        elif isinstance(source, bytes) or isinstance(source, bytearray):
            file_format = ResourceType.GFF if any(x for x in GFFContent if x.value == source[:4].decode('ascii', 'ignore')) else ResourceType.GFF_XML
        elif isinstance(source, BinaryReader):
            file_header = source.read_string(4)
            file_format = ResourceType.GFF if any(x.value == file_header for x in GFFContent) else ResourceType.GFF_XML
            source.skip(-4)
        else:
            file_format = ResourceType.INVALID
    except IOError:
        file_format = ResourceType.INVALID

    return file_format


def load_gff(source: SOURCE_TYPES, offset: int = 0) -> GFF:
    """
    Returns an GFF instance from the source. The file format (binary or xml) is automatically determined before parsing
    the data.

    Args:
        source: The source of the data.
        offset: The byte offset of the file inside the data.

    Raises:
        ValueError: If the file was corrupted or in an unsupported format.

    Returns:
        An GFF instance.
    """
    file_format = detect_gff(source, offset)

    try:
        if file_format == ResourceType.GFF:
            return GFFBinaryReader(source, offset).load()
        elif file_format == ResourceType.GFF_XML:
            return GFFXMLReader(source).load()
        else:
            raise ValueError
    except (IOError, ValueError):
        raise ValueError("Tried to load an unsupported or corrupted GFF file.")


def write_gff(gff: GFF, target: TARGET_TYPES, file_format: ResourceType = ResourceType.GFF) -> None:
    """
    Writes the GFF data to the target location with the specified format (binary or xml).

    Args:
        gff: The GFF file being written.
        target: The location to write the data to.
        file_format: The file format.

    Raises:
        ValueError: If an unsupported file format was given.
    """
    if file_format == ResourceType.GFF:
        GFFBinaryWriter(gff, target).write()
    elif file_format == ResourceType.GFF_XML:
        GFFXMLWriter(gff, target).write()
    else:
        raise ValueError("Unsupported format specified; use GFF or GFF_XML.")
