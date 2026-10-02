from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from harness import generate_enriched_toc


_TOC = """---
generator: db-snooper
database: neutron
---

Relationships: lines 12-58
`agents` (rows=129): lines 60-96
`vips` (rows=1): lines 1104-1136
Summary: lines 1138-1138
"""


class EnrichedTocTests(unittest.TestCase):
    def test_prompt_pins_strict_format_and_sibling_contrast(self) -> None:
        prompt = generate_enriched_toc._prompt("dw", 16)
        self.assertIn("one description line per table, in the `/inputs/toc.md` order", prompt)
        self.assertIn("`table_name`: one short description", prompt)
        self.assertIn('"Each row", "One row", or "This row"', prompt)
        self.assertIn("how that table differs", prompt)
        self.assertIn("name its source table in backticks", prompt)
        self.assertIn("re-explain that family in every", prompt)
        self.assertIn('not "newer LBaaS pool"', prompt)
        self.assertIn("no header, no markdown fences", prompt)

    def test_parse_accepts_exact_table_set(self) -> None:
        parsed = generate_enriched_toc.parse_descriptions(
            "`agents`: A Neutron agent per host: type, config, heartbeat state.\n"
            "\n"
            "`vips`: An LB-v1 virtual IP: address, protocol, port, pool link.\n",
            ["agents", "vips"],
        )
        self.assertEqual(parsed, {
            "agents": "A Neutron agent per host: type, config, heartbeat state.",
            "vips": "An LB-v1 virtual IP: address, protocol, port, pool link.",
        })

    def test_parse_rejects_missing_extra_malformed_and_overlong(self) -> None:
        with self.assertRaisesRegex(ValueError, "no description for 1 table"):
            generate_enriched_toc.parse_descriptions("`agents`: x", ["agents", "vips"])
        with self.assertRaisesRegex(ValueError, "unknown table"):
            generate_enriched_toc.parse_descriptions(
                "`agents`: x\n`ghost`: y", ["agents"])
        with self.assertRaisesRegex(ValueError, "not a `table`: description entry"):
            generate_enriched_toc.parse_descriptions("agents: x", ["agents"])
        with self.assertRaisesRegex(ValueError, "chars"):
            generate_enriched_toc.parse_descriptions(
                f"`agents`: {'x' * 241}", ["agents"])
        with self.assertRaisesRegex(ValueError, "more than once"):
            generate_enriched_toc.parse_descriptions("`agents`: x\n`agents`: y", ["agents"])
        for opener in ("Each row represents an agent.", "One row per agent.",
                       "This single row records the schema version."):
            with self.assertRaisesRegex(ValueError, "row-opener"):
                generate_enriched_toc.parse_descriptions(f"`agents`: {opener}", ["agents"])

    def test_merge_appends_descriptions_and_preserves_structure(self) -> None:
        merged = generate_enriched_toc.merge_toc(_TOC, {
            "agents": "A Neutron agent per host: type, config, heartbeat state.",
            "vips": "An LB-v1 virtual IP: address, protocol, port, pool link.",
        })
        lines = merged.splitlines()
        self.assertEqual(lines[0], "---")
        self.assertTrue(any(line.startswith("enriched_model: ") for line in lines))
        self.assertTrue(any(line.startswith("toc_sha256: ") for line in lines))
        self.assertIn("Relationships: lines 12-58", merged)
        self.assertIn("Summary: lines 1138-1138", merged)
        self.assertIn("`agents` (rows=129): lines 60-96 — A Neutron agent per host: "
                      "type, config, heartbeat state.", merged)
        self.assertIn("`vips` (rows=1): lines 1104-1136 — An LB-v1 virtual IP: "
                      "address, protocol, port, pool link.", merged)

    def test_merge_leaves_undescribed_toc_untouched(self) -> None:
        merged = generate_enriched_toc.merge_toc(_TOC, {"agents": "A Neutron agent per host."})
        self.assertIn("`vips` (rows=1): lines 1104-1136\n", merged)

    def test_resolved_toc_prefers_enriched_when_present(self) -> None:
        from harness import config
        with tempfile.TemporaryDirectory() as tmp:
            profiles = Path(tmp) / "profiles"
            generated = Path(tmp) / "generated-metadata"
            profiles.mkdir()
            plain = profiles / "neutron.toc.md"
            plain.write_text("plain\n", encoding="utf-8")
            with (patch.object(config, "PROFILES_DIR", profiles),
                  patch.object(config, "GENERATED_METADATA_DIR", generated)):
                self.assertEqual(config.resolved_toc_path_for("neutron"), plain)
                generated.mkdir()
                enriched = generated / "neutron.toc.md"
                enriched.write_text("enriched\n", encoding="utf-8")
                self.assertEqual(config.resolved_toc_path_for("neutron"), enriched)

    def test_every_config_attribute_referenced_exists(self) -> None:
        # run() needs docker/mysql, so its attr lookups are otherwise only
        # exercised for real; catch typos statically instead.
        import inspect
        import re as _re

        from harness import config

        used = set(_re.findall(r"config\.(\w+)", inspect.getsource(generate_enriched_toc)))
        missing = sorted(name for name in used if not hasattr(config, name))
        self.assertEqual(missing, [])

    def test_only_markdown_inputs_are_mounted(self) -> None:
        argv = generate_enriched_toc._docker_argv("neutron", 16, Path("generated-metada"))
        mounts = [argv[i + 1] for i, arg in enumerate(argv) if arg == "-v"]
        self.assertEqual(len(mounts), 6)
        self.assertEqual(argv[argv.index("--entrypoint") + 1], "pi")
        self.assertNotIn("json", argv)
        self.assertTrue(any("profiles/neutron.md:/inputs/profile.md:ro" in mount for mount in mounts))
        self.assertTrue(any("profiles/neutron.toc.md:/inputs/toc.md:ro" in mount for mount in mounts))
        self.assertTrue(any("schema-links/neutron.md:/inputs/schema-links.md:ro" in mount for mount in mounts))
        self.assertFalse(any("/data/" in mount or mount.endswith(".json") for mount in mounts))


if __name__ == "__main__":
    unittest.main()
