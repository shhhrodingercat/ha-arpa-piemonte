"""Tests for repository metadata and translation consistency."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INTEGRATION = ROOT / "custom_components" / "arpa_piemonte"


def load_json(path: Path) -> dict:
    """Load a JSON file from the repository."""
    return json.loads(path.read_text(encoding="utf-8"))


def test_manifest_has_required_project_metadata() -> None:
    """The integration manifest must identify this custom integration."""
    manifest = load_json(INTEGRATION / "manifest.json")

    assert manifest["domain"] == "arpa_piemonte"
    assert manifest["name"] == "ARPA Piemonte"
    assert manifest["config_flow"] is True
    assert manifest["version"]
    assert manifest["codeowners"] == ["@shhhrodingercat"]


def test_hacs_metadata_is_valid() -> None:
    """HACS metadata must be valid JSON and name the integration."""
    hacs = load_json(ROOT / "hacs.json")

    assert hacs["name"] == "ARPA Piemonte"


def test_translation_files_are_valid_and_have_matching_keys() -> None:
    """English and Italian translations must expose the same config keys."""
    english = load_json(INTEGRATION / "translations" / "en.json")
    italian = load_json(INTEGRATION / "translations" / "it.json")

    assert english.keys() == italian.keys()
    assert english["config"].keys() == italian["config"].keys()
    assert english["config"]["step"].keys() == italian["config"]["step"].keys()
    assert english["config"]["abort"].keys() == italian["config"]["abort"].keys()
