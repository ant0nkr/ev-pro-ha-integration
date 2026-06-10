"""Tests for byd_ev_pro/const.py."""
import importlib.util
from pathlib import Path

# Load const.py directly from its file path. Importing it through the package
# (`custom_components.byd_ev_pro.const`) would execute the package __init__,
# which pulls in homeassistant — not available in a plain test environment.
# const.py has no homeassistant dependency, so loading it standalone is enough.
_CONST_PATH = (
    Path(__file__).resolve().parents[1]
    / "custom_components"
    / "byd_ev_pro"
    / "const.py"
)
_spec = importlib.util.spec_from_file_location("byd_ev_pro_const", _CONST_PATH)
const = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(const)

CABIN_TEMP_SOURCE_MAP = const.CABIN_TEMP_SOURCE_MAP
SUNROOF_STATE_MAP = const.SUNROOF_STATE_MAP
SUNSHADE_STATE_MAP = const.SUNSHADE_STATE_MAP
resolve_cabin_temp_source = const.resolve_cabin_temp_source


def test_sunroof_state_map_zero_means_not_equipped():
    assert SUNROOF_STATE_MAP[0] == "Not Equipped"
    assert SUNROOF_STATE_MAP[1] == "Open"


def test_sunshade_state_map_zero_means_not_equipped():
    assert SUNSHADE_STATE_MAP[0] == "Not Equipped"
    assert SUNSHADE_STATE_MAP[1] == "Open"


def test_cabin_temp_source_map_values():
    assert CABIN_TEMP_SOURCE_MAP[0] == "none"
    assert CABIN_TEMP_SOURCE_MAP[1] == "car"
    assert CABIN_TEMP_SOURCE_MAP[2] == "tbox"


def test_resolve_cabin_temp_source_present():
    assert resolve_cabin_temp_source({"cabin_temp_source": 1}) == "car"
    assert resolve_cabin_temp_source({"cabin_temp_source": 2}) == "tbox"
    assert resolve_cabin_temp_source({"cabin_temp_source": 0}) == "none"


def test_resolve_cabin_temp_source_absent_is_none():
    # Legacy payloads omit the source field entirely -> untagged -> "none".
    assert resolve_cabin_temp_source({}) == "none"
    assert resolve_cabin_temp_source({"cabin_temp_source": None}) == "none"


def test_resolve_cabin_temp_source_unknown_value_is_none():
    assert resolve_cabin_temp_source({"cabin_temp_source": 9}) == "none"
    assert resolve_cabin_temp_source({"cabin_temp_source": "bad"}) == "none"
