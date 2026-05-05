"""Tests for byd_ev_pro/const.py."""
import sys
from pathlib import Path

# Allow `from custom_components.byd_ev_pro.const import ...` when running from
# the repo root without a package install (HACS components are not pip
# packages).
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from custom_components.byd_ev_pro.const import (
    SUNROOF_STATE_MAP,
    SUNSHADE_STATE_MAP,
)


def test_sunroof_state_map_zero_means_not_equipped():
    assert SUNROOF_STATE_MAP[0] == "Not Equipped"
    assert SUNROOF_STATE_MAP[1] == "Open"


def test_sunshade_state_map_zero_means_not_equipped():
    assert SUNSHADE_STATE_MAP[0] == "Not Equipped"
    assert SUNSHADE_STATE_MAP[1] == "Open"
