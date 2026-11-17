import json
from pathlib import Path
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
CHANGE_GUARD = "{if previous_extruder >= 0 && next_extruder >= 0 && previous_extruder != next_extruder}"


class FlushTriggerTests(unittest.TestCase):
    def assert_change_only(self, settings):
        self.assertEqual(settings["time_flush_interval"], "0")
        self.assertEqual(settings["time_flush_gcode"], "")
        code = settings["change_filament_gcode"]
        self.assertIn(CHANGE_GUARD, code)
        self.assertLess(code.index(CHANGE_GUARD), code.index("; I8_SIDE_PURGE_BEGIN"))
        self.assertIn("G1 E{15 - 10}", code)

    def test_json_presets(self):
        for path in ROOT.glob("presets/*/*machine.json"):
            with self.subTest(path=path):
                self.assert_change_only(json.loads(path.read_text()))

    def test_embedded_3mf_presets(self):
        for path in ROOT.glob("presets/*/*.3mf"):
            with zipfile.ZipFile(path) as archive:
                self.assertIsNone(archive.testzip())
                for name in ("Metadata/project_settings.config", "Metadata/machine_settings_1.config"):
                    with self.subTest(path=path, name=name):
                        self.assert_change_only(json.loads(archive.read(name)))

    def test_standalone_templates_match_presets(self):
        for mode in ("with-tower", "no-tower"):
            standalone = (ROOT / "gcode" / f"sparkx-i8-{mode}-change-filament.txt").read_text()
            preset = json.loads(next(ROOT.glob(f"presets/{mode}/*machine.json")).read_text())
            active = preset["change_filament_gcode"].split("; I8_ACTIVE_BEGIN\n")[1].split("; I8_ACTIVE_END")[0]
            self.assertEqual(standalone.split("\n\n", 1)[1], active)
            self.assertTrue(active.startswith(CHANGE_GUARD))


if __name__ == "__main__":
    unittest.main()
