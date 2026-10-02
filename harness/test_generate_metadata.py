from __future__ import annotations

import unittest
from pathlib import Path
from unittest.mock import patch

from harness import generate_metadata


class MetadataSandboxTests(unittest.TestCase):
    def test_prompt_contrasts_only_ambiguous_sibling_tables(self) -> None:
        prompt = generate_metadata._prompt("dw", 12)
        self.assertIn("contrast their purpose, row grain", prompt)
        self.assertIn("do not enumerate", prompt)
        self.assertIn("instead of blanket default join types", prompt)

    @patch("harness.generate_metadata.uuid.uuid4", return_value=type("U", (), {"hex": "test"})())
    def test_only_markdown_inputs_are_mounted(self, _uuid) -> None:
        argv = generate_metadata._docker_argv("neutron", 12, Path("generated-metada"))
        mounts = [argv[i + 1] for i, arg in enumerate(argv) if arg == "-v"]
        self.assertEqual(len(mounts), 5)
        self.assertEqual(argv[argv.index("--entrypoint") + 1], "pi")
        self.assertNotIn("json", argv)
        self.assertTrue(any("profiles/neutron.md:/inputs/profile.md:ro" in mount for mount in mounts))
        self.assertTrue(any("schema-links/neutron.md:/inputs/schema-links.md:ro" in mount for mount in mounts))
        self.assertFalse(any("/data/" in mount or mount.endswith(".json") for mount in mounts))

if __name__ == "__main__":
    unittest.main()
