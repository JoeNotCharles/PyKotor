import os
from unittest import TestCase

from pykotor.common.language import LocalizedString
from pykotor.extract.capsule import Capsule
from pykotor.extract.file import ResourceIdentifier
from pykotor.extract.installation import Installation, SearchLocation
from pykotor.resource.type import ResourceType
from pykotor.tools.misc import is_bif_file, is_nss_file


class TestInstallation(TestCase):
    def setUp(self) -> None:
        path = os.environ.get("K1_PATH")
        self.installation = Installation(path)

        if not os.path.exists(f"self.installation.override_path(){nwscript.nss}"):
            raise ValueError("Place nwscript.nss in override folder before testing.")

    def test_resource(self):
        installation = self.installation

        self.assertIsNone(installation.resource("c_bantha", ResourceType.UTC, []))
        self.assertIsNotNone(installation.resource("c_bantha", ResourceType.UTC))

        self.assertIsNotNone(
            installation.resource("c_bantha", ResourceType.UTC, [SearchLocation.CHITIN])
        )
        self.assertIsNone(installation.resource("xxx", ResourceType.UTC, [SearchLocation.CHITIN]))
        self.assertIsNotNone(
            installation.resource("m13aa", ResourceType.ARE, [SearchLocation.MODULES])
        )
        self.assertIsNone(installation.resource("xxx", ResourceType.ARE, [SearchLocation.MODULES]))
        self.assertIsNotNone(
            installation.resource("nwscript", ResourceType.NSS, [SearchLocation.OVERRIDE])
        )
        self.assertIsNone(installation.resource("xxx", ResourceType.NSS, [SearchLocation.OVERRIDE]))
        self.assertIsNotNone(
            installation.resource("NM03ABCITI06004_", ResourceType.WAV, [SearchLocation.VOICE])
        )
        self.assertIsNone(installation.resource("xxx", ResourceType.WAV, [SearchLocation.VOICE]))
        self.assertIsNotNone(
            installation.resource("P_hk47_POIS", ResourceType.WAV, [SearchLocation.SOUND])
        )
        self.assertIsNone(installation.resource("xxx", ResourceType.WAV, [SearchLocation.SOUND]))
        self.assertIsNotNone(
            installation.resource("mus_theme_carth", ResourceType.WAV, [SearchLocation.MUSIC])
        )
        self.assertIsNone(installation.resource("xxx", ResourceType.WAV, [SearchLocation.MUSIC]))
        self.assertIsNotNone(
            installation.resource("n_gendro_coms1", ResourceType.LIP, [SearchLocation.LIPS])
        )
        self.assertIsNone(installation.resource("xxx", ResourceType.LIP, [SearchLocation.LIPS]))
        self.assertIsNotNone(
            installation.resource("darkjedi", ResourceType.SSF, [SearchLocation.RIMS])
        )
        self.assertIsNone(installation.resource("xxx", ResourceType.SSF, [SearchLocation.RIMS]))
        self.assertIsNotNone(
            installation.resource("blood", ResourceType.TPC, [SearchLocation.TEXTURES_TPA])
        )
        self.assertIsNone(
            installation.resource("xxx", ResourceType.TPC, [SearchLocation.TEXTURES_TPA])
        )
        self.assertIsNotNone(
            installation.resource("blood", ResourceType.TPC, [SearchLocation.TEXTURES_TPB])
        )
        self.assertIsNone(
            installation.resource("xxx", ResourceType.TPC, [SearchLocation.TEXTURES_TPB])
        )
        self.assertIsNotNone(
            installation.resource("blood", ResourceType.TPC, [SearchLocation.TEXTURES_TPC])
        )
        self.assertIsNone(
            installation.resource("xxx", ResourceType.TPC, [SearchLocation.TEXTURES_TPC])
        )
        self.assertIsNotNone(
            installation.resource("PO_PCarth", ResourceType.TPC, [SearchLocation.TEXTURES_GUI])
        )
        self.assertIsNone(
            installation.resource("xxx", ResourceType.TPC, [SearchLocation.TEXTURES_GUI])
        )

        self.assertIsNotNone(
            installation.resource(
                "nwscript",
                ResourceType.NSS,
                [SearchLocation.CUSTOM_FOLDERS],
                folders=[installation.override_path()],
            ).data
        )
        self.assertIsNotNone(
            installation.resource(
                "m13aa",
                ResourceType.ARE,
                [SearchLocation.CUSTOM_MODULES],
                capsules=[Capsule(f"{installation.module_path()}danm13.rim")],
            ).data
        )

        self.assertTrue(
            is_bif_file(
                installation.resource(
                    "nwscript", ResourceType.NSS, [SearchLocation.CHITIN, SearchLocation.OVERRIDE]
                ).filepath
        ))
        self.assertTrue(
            is_nss_file(
                installation.resource(
                    "nwscript", ResourceType.NSS, [SearchLocation.OVERRIDE, SearchLocation.CHITIN]
                ).filepath
        ))

    def test_resources(self):
        installation = self.installation

        chitin_resources = [
            ResourceIdentifier.from_path("c_bantha.utc"),
            ResourceIdentifier.from_path("x.utc"),
        ]
        chitin_results = installation.resources(chitin_resources, [SearchLocation.CHITIN])
        self._extracted_from_test_locations_9(chitin_results, "c_bantha.utc", "x.utc")
        modules_resources = [
            ResourceIdentifier.from_path("m01aa.are"),
            ResourceIdentifier.from_path("x.tpc"),
        ]
        modules_results = installation.resources(modules_resources, [SearchLocation.MODULES])
        self._extracted_from_test_locations_9(modules_results, "m01aa.are", "x.tpc")
        override_resources = [
            ResourceIdentifier.from_path("nwscript.nss"),
            ResourceIdentifier.from_path("x.tpc"),
        ]
        override_results = installation.resources(override_resources, [SearchLocation.OVERRIDE])
        self._extracted_from_test_locations_9(
            override_results, "nwscript.nss", "x.tpc"
        )
        voices_resources = [
            ResourceIdentifier.from_path("NM17AE04NI04008_.wav"),
            ResourceIdentifier.from_path("x.mp3"),
        ]
        voices_results = installation.resources(voices_resources, [SearchLocation.VOICE])
        self._extracted_from_test_locations_9(
            voices_results, "NM17AE04NI04008_.wav", "x.mp3"
        )
        music_resources = [
            ResourceIdentifier.from_path("mus_theme_carth.wav"),
            ResourceIdentifier.from_path("x.mp3"),
        ]
        music_results = installation.resources(music_resources, [SearchLocation.MUSIC])
        self._extracted_from_test_locations_9(
            music_results, "mus_theme_carth.wav", "x.mp3"
        )
        sounds_resources = [
            ResourceIdentifier.from_path("P_ZAALBAR_POIS.wav"),
            ResourceIdentifier.from_path("x.mp3"),
        ]
        sounds_results = installation.resources(sounds_resources, [SearchLocation.SOUND])
        self._extracted_from_test_locations_9(
            sounds_results, "P_ZAALBAR_POIS.wav", "x.mp3"
        )
        lips_resources = [
            ResourceIdentifier.from_path("n_gendro_coms1.lip"),
            ResourceIdentifier.from_path("x.lip"),
        ]
        lips_results = installation.resources(lips_resources, [SearchLocation.LIPS])
        self._extracted_from_test_locations_9(
            lips_results, "n_gendro_coms1.lip", "x.lip"
        )
        rims_resources = [
            ResourceIdentifier.from_path("darkjedi.ssf"),
            ResourceIdentifier.from_path("x.ssf"),
        ]
        rims_results = installation.resources(rims_resources, [SearchLocation.RIMS])
        self._extracted_from_test_locations_9(rims_results, "darkjedi.ssf", "x.ssf")
        texa_resources = [
            ResourceIdentifier.from_path("blood.tpc"),
            ResourceIdentifier.from_path("x.tpc"),
        ]
        texa_results = installation.resources(texa_resources, [SearchLocation.TEXTURES_TPA])
        self._extracted_from_test_locations_9(texa_results, "blood.tpc", "x.tpc")
        texb_resources = [
            ResourceIdentifier.from_path("blood.tpc"),
            ResourceIdentifier.from_path("x.tpc"),
        ]
        texb_results = installation.resources(texb_resources, [SearchLocation.TEXTURES_TPB])
        self._extracted_from_test_locations_9(texb_results, "blood.tpc", "x.tpc")
        texc_resources = [
            ResourceIdentifier.from_path("blood.tpc"),
            ResourceIdentifier.from_path("x.tpc"),
        ]
        texc_results = installation.resources(texc_resources, [SearchLocation.TEXTURES_TPC])
        self._extracted_from_test_locations_9(texc_results, "blood.tpc", "x.tpc")
        texg_resources = [
            ResourceIdentifier.from_path("1024x768back.tpc"),
            ResourceIdentifier.from_path("x.tpc"),
        ]
        texg_results = installation.resources(texg_resources, [SearchLocation.TEXTURES_GUI])
        self._extracted_from_test_locations_9(
            texg_results, "1024x768back.tpc", "x.tpc"
        )
        capsules = [Capsule(f"{installation.module_path()}danm13.rim")]
        capsules_resources = [
            ResourceIdentifier.from_path("m13aa.are"),
            ResourceIdentifier.from_path("xyz.ifo"),
        ]
        capsules_results = installation.resources(
            capsules_resources, [SearchLocation.CUSTOM_MODULES], capsules=capsules
        )
        self._extracted_from_test_locations_9(capsules_results, "m13aa.are", "xyz.ifo")
        folders = [installation.override_path()]
        folders_resources = [
            ResourceIdentifier.from_path("nwscript.nss"),
            ResourceIdentifier.from_path("x.utc"),
        ]
        folders_results = installation.resources(
            folders_resources, [SearchLocation.CUSTOM_FOLDERS], folders=folders
        )
        self._extracted_from_test_locations_9(folders_results, "nwscript.nss", "x.utc")

    def test_location(self):
        installation = self.installation

        self.assertFalse(installation.location("m13aa", ResourceType.ARE, []))
        self.assertTrue(installation.location("m13aa", ResourceType.ARE))

        self.assertTrue(installation.location("m13aa", ResourceType.ARE, [SearchLocation.MODULES]))

        self.assertTrue(
            installation.location("c_bantha", ResourceType.UTC, [SearchLocation.CHITIN])
        )
        self.assertFalse(installation.location("xxx", ResourceType.UTC, [SearchLocation.CHITIN]))
        self.assertTrue(installation.location("m13aa", ResourceType.ARE, [SearchLocation.MODULES]))
        self.assertFalse(installation.location("xxx", ResourceType.ARE, [SearchLocation.MODULES]))
        self.assertTrue(
            installation.location("nwscript", ResourceType.NSS, [SearchLocation.OVERRIDE])
        )
        self.assertFalse(installation.location("xxx", ResourceType.NSS, [SearchLocation.OVERRIDE]))
        self.assertTrue(
            installation.location("NM03ABCITI06004_", ResourceType.WAV, [SearchLocation.VOICE])
        )
        self.assertFalse(installation.location("xxx", ResourceType.WAV, [SearchLocation.VOICE]))
        self.assertTrue(
            installation.location("P_hk47_POIS", ResourceType.WAV, [SearchLocation.SOUND])
        )
        self.assertFalse(installation.location("xxx", ResourceType.WAV, [SearchLocation.SOUND]))
        self.assertTrue(
            installation.location("mus_theme_carth", ResourceType.WAV, [SearchLocation.MUSIC])
        )
        self.assertFalse(installation.location("xxx", ResourceType.WAV, [SearchLocation.MUSIC]))
        self.assertTrue(
            installation.location("n_gendro_coms1", ResourceType.LIP, [SearchLocation.LIPS])
        )
        self.assertFalse(installation.location("xxx", ResourceType.LIP, [SearchLocation.LIPS]))
        self.assertTrue(installation.location("darkjedi", ResourceType.SSF, [SearchLocation.RIMS]))
        self.assertFalse(installation.location("xxx", ResourceType.SSF, [SearchLocation.RIMS]))
        self.assertTrue(
            installation.location("blood", ResourceType.TPC, [SearchLocation.TEXTURES_TPA])
        )
        self.assertFalse(
            installation.location("xxx", ResourceType.TPC, [SearchLocation.TEXTURES_TPA])
        )
        self.assertTrue(
            installation.location("blood", ResourceType.TPC, [SearchLocation.TEXTURES_TPB])
        )
        self.assertFalse(
            installation.location("xxx", ResourceType.TPC, [SearchLocation.TEXTURES_TPB])
        )
        self.assertTrue(
            installation.location("blood", ResourceType.TPC, [SearchLocation.TEXTURES_TPC])
        )
        self.assertFalse(
            installation.location("xxx", ResourceType.TPC, [SearchLocation.TEXTURES_TPC])
        )
        self.assertTrue(
            installation.location("PO_PCarth", ResourceType.TPC, [SearchLocation.TEXTURES_GUI])
        )
        self.assertFalse(
            installation.location("xxx", ResourceType.TPC, [SearchLocation.TEXTURES_GUI])
        )

    def test_locations(self):
        installation = self.installation

        chitin_resources = [
            ResourceIdentifier.from_path("c_bantha.utc"),
            ResourceIdentifier.from_path("x.utc"),
        ]
        chitin_results = installation.locations(chitin_resources, [SearchLocation.CHITIN])
        self._extracted_from_test_locations_9(chitin_results, "c_bantha.utc", "x.utc")
        modules_resources = [
            ResourceIdentifier.from_path("m01aa.are"),
            ResourceIdentifier.from_path("x.tpc"),
        ]
        modules_results = installation.locations(modules_resources, [SearchLocation.MODULES])
        self._extracted_from_test_locations_9(modules_results, "m01aa.are", "x.tpc")
        override_resources = [
            ResourceIdentifier.from_path("nwscript.nss"),
            ResourceIdentifier.from_path("x.tpc"),
        ]
        override_results = installation.locations(override_resources, [SearchLocation.OVERRIDE])
        self._extracted_from_test_locations_9(
            override_results, "nwscript.nss", "x.tpc"
        )
        voices_resources = [
            ResourceIdentifier.from_path("NM17AE04NI04008_.wav"),
            ResourceIdentifier.from_path("x.mp3"),
        ]
        voices_results = installation.locations(voices_resources, [SearchLocation.VOICE])
        self._extracted_from_test_locations_9(
            voices_results, "NM17AE04NI04008_.wav", "x.mp3"
        )
        music_resources = [
            ResourceIdentifier.from_path("mus_theme_carth.wav"),
            ResourceIdentifier.from_path("x.mp3"),
        ]
        music_results = installation.locations(music_resources, [SearchLocation.MUSIC])
        self._extracted_from_test_locations_9(
            music_results, "mus_theme_carth.wav", "x.mp3"
        )
        sounds_resources = [
            ResourceIdentifier.from_path("P_ZAALBAR_POIS.wav"),
            ResourceIdentifier.from_path("x.mp3"),
        ]
        sounds_results = installation.locations(sounds_resources, [SearchLocation.SOUND])
        self._extracted_from_test_locations_9(
            sounds_results, "P_ZAALBAR_POIS.wav", "x.mp3"
        )
        lips_resources = [
            ResourceIdentifier.from_path("n_gendro_coms1.lip"),
            ResourceIdentifier.from_path("x.lip"),
        ]
        lips_results = installation.locations(lips_resources, [SearchLocation.LIPS])
        self._extracted_from_test_locations_9(
            lips_results, "n_gendro_coms1.lip", "x.lip"
        )
        rims_resources = [
            ResourceIdentifier.from_path("darkjedi.ssf"),
            ResourceIdentifier.from_path("x.ssf"),
        ]
        rims_results = installation.locations(rims_resources, [SearchLocation.RIMS])
        self._extracted_from_test_locations_9(rims_results, "darkjedi.ssf", "x.ssf")
        texa_resources = [
            ResourceIdentifier.from_path("blood.tpc"),
            ResourceIdentifier.from_path("x.tpc"),
        ]
        texa_results = installation.locations(texa_resources, [SearchLocation.TEXTURES_TPA])
        self._extracted_from_test_locations_9(texa_results, "blood.tpc", "x.tpc")
        texb_resources = [
            ResourceIdentifier.from_path("blood.tpc"),
            ResourceIdentifier.from_path("x.tpc"),
        ]
        texb_results = installation.locations(texb_resources, [SearchLocation.TEXTURES_TPB])
        self._extracted_from_test_locations_9(texb_results, "blood.tpc", "x.tpc")
        texc_resources = [
            ResourceIdentifier.from_path("blood.tpc"),
            ResourceIdentifier.from_path("x.tpc"),
        ]
        texc_results = installation.locations(texc_resources, [SearchLocation.TEXTURES_TPC])
        self._extracted_from_test_locations_9(texc_results, "blood.tpc", "x.tpc")
        texg_resources = [
            ResourceIdentifier.from_path("1024x768back.tpc"),
            ResourceIdentifier.from_path("x.tpc"),
        ]
        texg_results = installation.locations(texg_resources, [SearchLocation.TEXTURES_GUI])
        self._extracted_from_test_locations_9(
            texg_results, "1024x768back.tpc", "x.tpc"
        )
        capsules = [Capsule(installation.module_path() + "danm13.rim")]
        capsules_resources = [
            ResourceIdentifier.from_path("m13aa.are"),
            ResourceIdentifier.from_path("xyz.ifo"),
        ]
        capsules_results = installation.locations(
            capsules_resources, [SearchLocation.CUSTOM_MODULES], capsules=capsules
        )
        self._extracted_from_test_locations_9(capsules_results, "m13aa.are", "xyz.ifo")
        folders = [installation.override_path()]
        folders_resources = [
            ResourceIdentifier.from_path("nwscript.nss"),
            ResourceIdentifier.from_path("x.utc"),
        ]
        folders_results = installation.locations(
            folders_resources, [SearchLocation.CUSTOM_FOLDERS], folders=folders
        )
        self._extracted_from_test_locations_9(folders_results, "nwscript.nss", "x.utc")

    # TODO Rename this here and in `test_resources` and `test_locations`
    def _extracted_from_test_locations_9(self, arg0, arg1, arg2):
        self.assertTrue(arg0[ResourceIdentifier.from_path(arg1)])
        self.assertFalse(arg0[ResourceIdentifier.from_path(arg2)])
        self.assertEqual(2, len(arg0))

    def test_texture(self):
        installation = self.installation

        self.assertIsNotNone(installation.texture("m03ae_03a_lm4", [SearchLocation.CHITIN]))
        self.assertIsNone(installation.texture("x", [SearchLocation.CHITIN]))

        self.assertIsNotNone(installation.texture("LEH_FLOOR01", [SearchLocation.TEXTURES_TPA]))
        self.assertIsNone(installation.texture("x", [SearchLocation.TEXTURES_TPA]))

        self.assertIsNotNone(installation.texture("LEH_Floor01", [SearchLocation.TEXTURES_TPB]))
        self.assertIsNone(installation.texture("x", [SearchLocation.TEXTURES_TPB]))

        self.assertIsNotNone(installation.texture("leh_floor01", [SearchLocation.TEXTURES_TPC]))
        self.assertIsNone(installation.texture("x", [SearchLocation.TEXTURES_TPC]))

        self.assertIsNotNone(installation.texture("bluearrow", [SearchLocation.TEXTURES_GUI]))
        self.assertIsNone(installation.texture("x", [SearchLocation.TEXTURES_GUI]))

    def test_textures(self):
        installation = self.installation

        chitin_textures = ["m03ae_03a_lm4", "x"]
        chitin_results = installation.textures(chitin_textures, [SearchLocation.CHITIN])
        self.assertIsNotNone(chitin_results["m03ae_03a_lm4"])
        self.assertIsNone(chitin_results["x"])
        self.assertEqual(2, len(chitin_results))

        tpa_textures = ["LEH_Floor01", "x"]
        tpa_results = installation.textures(tpa_textures, [SearchLocation.TEXTURES_TPA])
        self.assertIsNotNone(tpa_results["leh_floor01"])
        self.assertIsNone(tpa_results["x"])
        self.assertEqual(2, len(tpa_results))

        tpb_textures = ["LEH_Floor01", "x"]
        tpb_results = installation.textures(tpb_textures, [SearchLocation.TEXTURES_TPB])
        self.assertIsNotNone(tpb_results["leh_floor01"])
        self.assertIsNone(tpb_results["x"])
        self.assertEqual(2, len(tpb_results))

        tpc_textures = ["LEH_Floor01", "x"]
        tpc_results = installation.textures(tpc_textures, [SearchLocation.TEXTURES_TPC])
        self.assertIsNotNone(tpc_results["leh_floor01"])
        self.assertIsNone(tpc_results["x"])
        self.assertEqual(2, len(tpc_results))

        gui_textures = ["bluearrow", "x"]
        gui_results = installation.textures(gui_textures, [SearchLocation.TEXTURES_GUI])
        self.assertIsNotNone(gui_results["bluearrow"])
        self.assertIsNone(gui_results["x"])
        self.assertEqual(2, len(gui_results))

    def test_sounds(self):
        installation = self.installation

        chitin_sounds = ["as_an_dantext_01", "x"]
        chitin_results = installation.sounds(chitin_sounds, [SearchLocation.CHITIN])
        self.assertIsNotNone(chitin_results["as_an_dantext_01"])
        self.assertIsNone(chitin_results["x"])

        rim_sounds = ["FS_metal1", "x"]
        rim_results = installation.sounds(rim_sounds, [SearchLocation.RIMS])
        self.assertIsNotNone(rim_results["FS_metal1"])
        self.assertIsNone(rim_results["x"])

        sound_sounds = ["al_an_flybuzz_01", "x"]
        sound_results = installation.sounds(sound_sounds, [SearchLocation.SOUND])
        self.assertIsNotNone(sound_results["al_an_flybuzz_01"])
        self.assertIsNone(sound_results["x"])

        music_sounds = ["al_en_cityext", "x"]
        music_results = installation.sounds(music_sounds, [SearchLocation.MUSIC])
        self.assertIsNotNone(music_results["al_en_cityext"])
        self.assertIsNone(music_results["x"])

        voice_sounds = ["n_gengamm_scrm", "x"]
        voice_results = installation.sounds(voice_sounds, [SearchLocation.VOICE])
        self.assertIsNotNone(voice_results["n_gengamm_scrm"])
        self.assertIsNone(voice_results["x"])

    def test_string(self):
        installation = self.installation

        locstring1 = LocalizedString.from_invalid()
        locstring2 = LocalizedString.from_english("Some text.")
        locstring3 = LocalizedString(2)

        self.assertEqual("default text", installation.string(locstring1, "default text"))
        self.assertEqual("Some text.", installation.string(locstring2, "default text"))
        self.assertEqual(
            "ERROR: FATAL COMPILER ERROR", installation.string(locstring3, "default text")
        )

    def test_strings(self):
        installation = self.installation

        locstring1 = LocalizedString.from_invalid()
        locstring2 = LocalizedString.from_english("Some text.")
        locstring3 = LocalizedString(2)

        results = installation.strings([locstring1, locstring2, locstring3], "default text")
        self.assertEqual("default text", results[locstring1])
        self.assertEqual("Some text.", results[locstring2])
        self.assertEqual("ERROR: FATAL COMPILER ERROR", results[locstring3])
