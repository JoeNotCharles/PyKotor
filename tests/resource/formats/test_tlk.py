from unittest import TestCase

from pykotor.resource.type import ResourceType

from pykotor.common.language import Language
from pykotor.common.misc import ResRef
from pykotor.resource.formats.tlk import TLK, TLKEntry, detect_tlk, TLKBinaryReader, write_tlk, read_tlk, TLKXMLReader, \
    TLKJSONReader

BINARY_TEST_FILE = "../../files/test.tlk"
XML_TEST_FILE = "../../files/test.tlk.xml"
JSON_TEST_FILE = "../../files/test.tlk.json"


class TestTLK(TestCase):
    def test_resize(self):
        tlk = TLKBinaryReader(BINARY_TEST_FILE).load()
        self.assertEqual(len(tlk), 3)
        tlk.resize(4)
        self.assertEqual(len(tlk), 4)
        self.assertEqual(TLKEntry("qrstuvwxyz", ResRef("")), tlk[2])
        self.assertEqual(TLKEntry("", ResRef("")), tlk[3])
        tlk.resize(1)
        self.assertEqual(len(tlk), 1)
        self.assertEqual(TLKEntry("abcdef", ResRef("resref01")), tlk.get(0))
        self.assertIsNone(tlk.get(1))

    def test_binary_io(self):
        self.assertEqual(detect_tlk(BINARY_TEST_FILE), ResourceType.TLK)

        tlk = TLKBinaryReader(BINARY_TEST_FILE).load()
        self.validate_io(tlk)

        data = bytearray()
        write_tlk(tlk, data, ResourceType.TLK)
        tlk = read_tlk(data)
        self.validate_io(tlk)

    def test_xml_io(self):
        self.assertEqual(detect_tlk(XML_TEST_FILE), ResourceType.TLK_XML)

        tlk = TLKXMLReader(XML_TEST_FILE).load()
        self.validate_io(tlk)

        data = bytearray()
        write_tlk(tlk, data, ResourceType.TLK_XML)
        tlk = read_tlk(data)
        self.validate_io(tlk)

    def test_json_io(self):
        self.assertEqual(detect_tlk(JSON_TEST_FILE), ResourceType.TLK_JSON)

        tlk = TLKJSONReader(JSON_TEST_FILE).load()
        self.validate_io(tlk)

        data = bytearray()
        write_tlk(tlk, data, ResourceType.TLK_JSON)
        tlk = read_tlk(data)
        self.validate_io(tlk)

    def validate_io(self, tlk: TLK):
        self.assertIs(tlk.language, Language.ENGLISH)

        self.assertEqual(TLKEntry("abcdef", ResRef("resref01")), tlk[0])
        self.assertEqual(TLKEntry("ghijklmnop", ResRef("resref02")), tlk[1])
        self.assertEqual(TLKEntry("qrstuvwxyz", ResRef("")), tlk[2])
