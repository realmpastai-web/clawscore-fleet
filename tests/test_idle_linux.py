"""Unit tests for the idle-Linux fixture and discovery port."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from clawscore_fleet.fixtures.idle_linux import CHANGELOG_IDS, LAYOUTS, NAMES_FILE, build_fixture
from clawscore_fleet.idle_linux import (
    VERSION_SOURCE,
    _parse_schema_stdout,
    _path_owner,
    discover_all,
    idle_ok,
    published_schema_gate,
    scan_row,
)
from clawscore_fleet.versions import ROOT


def _names() -> list[str]:
    return [line.strip() for line in NAMES_FILE.read_text().splitlines() if line.strip()]


def _write_package(root: Path, rel: str, version: str) -> None:
    path = root / rel / "package.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"name": "openclaw", "version": version}) + "\n")


class IdleLinuxFixtureTest(unittest.TestCase):
    def test_two_runs_report_the_same_file_count(self) -> None:
        with tempfile.TemporaryDirectory(prefix="clawscore-idle-test-") as tmp:
            out = Path(tmp) / "fixture"
            first = build_fixture(out)
            first_files = [
                path for path in out.rglob("*") if path.is_file() and path.name != "FIXTURE_MANIFEST.txt"
            ]
            second = build_fixture(out)
            second_files = [
                path for path in out.rglob("*") if path.is_file() and path.name != "FIXTURE_MANIFEST.txt"
            ]
        self.assertEqual(first["files"], second["files"])
        self.assertEqual(first["dist_js"], second["dist_js"])
        self.assertEqual(first["files"], len(first_files))
        self.assertEqual(second["files"], len(second_files))
        self.assertEqual(first["dist_js"], len(_names()))
        self.assertFalse(first["version_in_package_json"])
        self.assertFalse(first["git_head_in_package_json"])

    def test_discovery_recovers_version_without_package_json(self) -> None:
        with tempfile.TemporaryDirectory(prefix="clawscore-idle-test-") as tmp:
            out = Path(tmp) / "fixture"
            build_fixture(out)
            loaded = json.loads((out / LAYOUTS["L3s"] / "package.json").read_text())
            self.assertNotIn("version", loaded)
            self.assertNotIn("gitHead", loaded)
            self.assertEqual(loaded["name"], "openclaw")
            for layout_id in ("L1", "L2", "L3"):
                versioned = json.loads((out / LAYOUTS[layout_id] / "package.json").read_text())
                self.assertEqual(versioned["version"], "2026.4.15")
                self.assertNotIn("gitHead", versioned)
            config = json.loads((next(out.rglob(".openclaw/openclaw.json"))).read_text())
            self.assertEqual(config["gateway"]["auth"]["token"], "")
            env_text = next(out.rglob(".openclaw/.env")).read_text()
            self.assertIn("OPENCLAW_GATEWAY_TOKEN=\n", env_text)
            self.assertIn("ANTHROPIC_API_KEY=\n", env_text)
            self.assertFalse((out / "proc").exists())
            self.assertFalse(list(out.rglob("*.pid")))
            owners = {"L1": "claw1", "L2": "claw2", "L3": "claw3", "L3s": "claw4"}
            for layout_id, user in owners.items():
                unit = out / "home" / user / ".config" / "systemd" / "user" / "openclaw-gateway.service"
                link = unit.parent / "default.target.wants" / "openclaw-gateway.service"
                self.assertTrue(unit.is_file(), layout_id)
                self.assertTrue(link.is_symlink(), layout_id)
                self.assertTrue((out / "var" / "lib" / "systemd" / "linger" / user).is_file(), layout_id)
                self.assertIn(LAYOUTS[layout_id], unit.read_text())
            linger = sorted(path.name for path in out.rglob("var/lib/systemd/linger/*"))
            self.assertEqual(linger, ["claw1", "claw2", "claw3", "claw4"])
            changelog = (out / LAYOUTS["L3s"] / "CHANGELOG.md").read_text().splitlines()
            pinned = [line.strip() for line in CHANGELOG_IDS.read_text().splitlines() if line.strip()]
            self.assertEqual(changelog, pinned)
            rows = discover_all(out)
            found = next(item for item in rows if item["install"] == LAYOUTS["L3s"])
            row = scan_row(found)
        self.assertEqual(row["state"], "idle")
        self.assertEqual(row["version_source"], VERSION_SOURCE)
        self.assertFalse(row["package_json_has_version"])
        self.assertEqual(row["version"], found["version"]["from_build_info"])
        self.assertGreaterEqual(row["dirlist_jaccard"], 0.99)
        self.assertEqual(found["idle"]["running_process_evidence"], 0)


class DiscoverAllTest(unittest.TestCase):
    def test_four_installer_layouts(self) -> None:
        with tempfile.TemporaryDirectory(prefix="clawscore-idle-test-") as tmp:
            out = Path(tmp) / "fixture"
            build_fixture(out)
            rows = discover_all(out)
        by_install = {item["install"]: item for item in rows}
        self.assertEqual(set(by_install), set(LAYOUTS.values()))
        self.assertEqual(len(rows), 4)
        for layout_id in ("L1", "L2", "L3"):
            item = by_install[LAYOUTS[layout_id]]
            self.assertEqual(item["resolved_version"], "2026.4.15")
            self.assertEqual(item["version_source"], "package.json")
            self.assertTrue(idle_ok(item))
        stripped = by_install[LAYOUTS["L3s"]]
        self.assertEqual(stripped["resolved_version"], "2026.4.15")
        self.assertEqual(stripped["version_source"], VERSION_SOURCE)
        self.assertTrue(idle_ok(stripped))
        self.assertFalse(stripped["version"]["package_json_has_version"])

    def test_depth_bound_and_walk_roots(self) -> None:
        with tempfile.TemporaryDirectory(prefix="clawscore-idle-test-") as tmp:
            root = Path(tmp)
            kept = "home/u/a/b/c/d/e/node_modules/openclaw"
            too_deep = "home/u/a/b/c/d/e/f/node_modules/openclaw"
            outside = "var/lib/node_modules/openclaw"
            self.assertEqual(len(Path(kept).parts), 9)
            self.assertEqual(len(Path(too_deep).parts), 10)
            _write_package(root, kept, "2026.4.15")
            _write_package(root, too_deep, "2026.4.15")
            _write_package(root, outside, "2026.4.15")
            rows = discover_all(root)
        self.assertEqual([item["install"] for item in rows], [kept])

    def test_stop_at_first_node_modules_openclaw(self) -> None:
        with tempfile.TemporaryDirectory(prefix="clawscore-idle-test-") as tmp:
            root = Path(tmp)
            outer = "home/claw2/.npm-global/lib/node_modules/openclaw"
            inner = outer + "/node_modules/openclaw"
            sibling = "opt/lib/node_modules/openclaw"
            self.assertLessEqual(len(Path(inner).parts), 9)
            _write_package(root, outer, "1.2.3")
            _write_package(root, inner, "9.9.9")
            _write_package(root, sibling, "4.5.6")
            rows = discover_all(root)
        installs = {item["install"]: item["resolved_version"] for item in rows}
        self.assertEqual(installs, {outer: "1.2.3", sibling: "4.5.6"})
        self.assertNotIn(inner, installs)


def _install_unit(
    root: Path,
    user: str,
    body: str,
    *,
    unit_name: str = "openclaw-gateway.service",
    enable: bool = True,
    linger: bool = True,
) -> None:
    unit_dir = root / "home" / user / ".config" / "systemd" / "user"
    unit = unit_dir / unit_name
    unit.parent.mkdir(parents=True, exist_ok=True)
    unit.write_text(body)
    if enable:
        link = unit_dir / "default.target.wants" / unit_name
        link.parent.mkdir(parents=True, exist_ok=True)
        if not link.exists():
            link.symlink_to(Path("..") / unit_name)
    if linger:
        marker = root / "var" / "lib" / "systemd" / "linger" / user
        marker.parent.mkdir(parents=True, exist_ok=True)
        marker.write_text("")


class SystemRootOwnerTest(unittest.TestCase):
    def test_renamed_system_owner_stays_idle(self) -> None:
        with tempfile.TemporaryDirectory(prefix="clawscore-idle-test-") as tmp:
            out = Path(tmp) / "fixture"
            build_fixture(out, system_owner="alice")
            self.assertFalse((out / "home" / "claw1").exists())
            self.assertTrue((out / "home" / "alice" / ".config" / "systemd" / "user" / "openclaw-gateway.service").is_file())
            self.assertTrue((out / "var" / "lib" / "systemd" / "linger" / "alice").is_file())
            rows = discover_all(out)
        by_install = {item["install"]: item for item in rows}
        found = by_install[LAYOUTS["L1"]]
        self.assertEqual((idle_ok(found), found["idle"]["linger_markers"]), (True, ["alice"]))
        self.assertTrue(found["idle"]["user_unit"])
        self.assertTrue(found["idle"]["enabled_symlink"])
        for layout_id, user in (("L2", "claw2"), ("L3", "claw3"), ("L3s", "claw4")):
            item = by_install[LAYOUTS[layout_id]]
            self.assertEqual(item["idle"]["linger_markers"], [user], layout_id)
            self.assertTrue(idle_ok(item), layout_id)

    def test_linger_without_referencing_unit_is_not_idle(self) -> None:
        rel = "usr/lib/node_modules/openclaw"
        with tempfile.TemporaryDirectory(prefix="clawscore-idle-test-") as tmp:
            root = Path(tmp)
            _write_package(root, rel, "2026.4.15")
            _install_unit(
                root,
                "bob",
                "[Service]\nExecStart=/usr/lib/node_modules/openclaw-extra/openclaw.mjs gateway\n",
            )
            rows = discover_all(root)
        self.assertEqual([item["install"] for item in rows], [rel])
        found = rows[0]
        self.assertEqual((idle_ok(found), found["idle"]["linger_markers"]), (False, []))

    def test_only_referencing_user_counts(self) -> None:
        rel = "usr/lib/node_modules/openclaw"
        with tempfile.TemporaryDirectory(prefix="clawscore-idle-test-") as tmp:
            root = Path(tmp)
            _write_package(root, rel, "2026.4.15")
            _install_unit(
                root,
                "nina",
                f"[Service]\nWorkingDirectory=/{rel}\n",
                unit_name="gateway.service",
            )
            _install_unit(
                root,
                "omar",
                "[Service]\nExecStart=/bin/true\nWorkingDirectory=/tmp\n",
                unit_name="other.service",
            )
            rows = discover_all(root)
        found = rows[0]
        self.assertEqual(found["install"], rel)
        self.assertEqual(found["idle"]["linger_markers"], ["nina"])
        self.assertNotIn("omar", found["idle"]["linger_markers"])
        self.assertTrue(idle_ok(found))


def _root_user_gateway(root: Path, rel: str, unit_exec: str, *, linger: bool = True) -> None:
    """Same fixture shape as inputs/clawscore-root-owner/gate_root_owner.py."""
    package = root / rel
    package.mkdir(parents=True)
    (package / "package.json").write_text(
        json.dumps({"name": "openclaw", "version": "2026.4.15", "bin": {"openclaw": "openclaw.mjs"}})
    )
    unit_dir = root / "root" / ".config" / "systemd" / "user"
    unit_dir.mkdir(parents=True)
    (unit_dir / "openclaw-gateway.service").write_text(f"[Service]\nExecStart={unit_exec} gateway\n")
    wants = unit_dir / "default.target.wants"
    wants.mkdir()
    (wants / "openclaw-gateway.service").symlink_to("../openclaw-gateway.service")
    if linger:
        marker = root / "var" / "lib" / "systemd" / "linger" / "root"
        marker.parent.mkdir(parents=True, exist_ok=True)
        marker.write_text("")


class RootOwnerGateTest(unittest.TestCase):
    def test_r1_system_install_root_unit(self) -> None:
        rel = "usr/lib/node_modules/openclaw"
        exe = "/usr/lib/node_modules/openclaw/openclaw.mjs"
        with tempfile.TemporaryDirectory(prefix="clawscore-root-owner-") as tmp:
            root = Path(tmp)
            _root_user_gateway(root, rel, exe)
            rows = discover_all(root)
        self.assertEqual([item["install"] for item in rows], [rel])
        found = rows[0]
        self.assertEqual((idle_ok(found), found["idle"]["linger_markers"]), (True, ["root"]))

    def test_r2_root_home_install(self) -> None:
        rel = "root/.npm-global/lib/node_modules/openclaw"
        exe = "/root/.npm-global/lib/node_modules/openclaw/openclaw.mjs"
        self.assertEqual(_path_owner(rel), "root")
        with tempfile.TemporaryDirectory(prefix="clawscore-root-owner-") as tmp:
            root = Path(tmp)
            _root_user_gateway(root, rel, exe)
            rows = discover_all(root)
        self.assertEqual([item["install"] for item in rows], [rel])
        found = rows[0]
        self.assertEqual((idle_ok(found), found["idle"]["linger_markers"]), (True, ["root"]))

    def test_c1_root_unit_no_linger(self) -> None:
        rel = "usr/lib/node_modules/openclaw"
        exe = "/usr/lib/node_modules/openclaw/openclaw.mjs"
        with tempfile.TemporaryDirectory(prefix="clawscore-root-owner-") as tmp:
            root = Path(tmp)
            _root_user_gateway(root, rel, exe, linger=False)
            rows = discover_all(root)
        found = rows[0]
        self.assertEqual(found["install"], rel)
        self.assertEqual((idle_ok(found), found["idle"]["linger_markers"]), (False, []))

    def test_c2_root_unit_other_path(self) -> None:
        rel = "usr/lib/node_modules/openclaw"
        exe = "/usr/lib/node_modules/openclaw-extra/openclaw.mjs"
        with tempfile.TemporaryDirectory(prefix="clawscore-root-owner-") as tmp:
            root = Path(tmp)
            _root_user_gateway(root, rel, exe)
            rows = discover_all(root)
        found = rows[0]
        self.assertEqual(found["install"], rel)
        self.assertEqual((idle_ok(found), found["idle"]["linger_markers"]), (False, []))


class PublishedSchemaGateTest(unittest.TestCase):
    def test_live_script_matches_frozen_output_and_parses_verdicts(self) -> None:
        gate = published_schema_gate()
        actuals = gate["actuals"]
        frozen = (ROOT / "inputs" / "rea-agent365-schema" / "gate-output.txt").read_text()
        parsed = _parse_schema_stdout(frozen)
        self.assertTrue(gate["pass"])
        self.assertEqual(actuals["exit_code"], 0)
        self.assertTrue(actuals["output_matches_frozen"])
        self.assertEqual(actuals["verdict_a"], parsed["verdict_a"])
        self.assertEqual(actuals["verdict_a_detail"], parsed["verdict_a_detail"])
        self.assertEqual(actuals["verdict_b"], parsed["verdict_b"])
        self.assertEqual(actuals["verdict_b_detail"], parsed["verdict_b_detail"])
        self.assertEqual(actuals["scope"], parsed["scope"])
        self.assertTrue(actuals["verdict_a"])
        self.assertTrue(actuals["verdict_b"])
        self.assertTrue(actuals["scope"])
        self.assertNotIn("mock-agent365", json.dumps(gate))


if __name__ == "__main__":
    unittest.main()
