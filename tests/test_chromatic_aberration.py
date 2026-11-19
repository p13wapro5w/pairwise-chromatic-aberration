import pytest
from postfx import chromatic_aberration as mod

CASES = [
    ("offset_50", 'm.offset_for_focal(50.0, 10.0) == approx(0.2)'),
    ("offset_25", 'm.offset_for_focal(25.0, 10.0) == approx(0.4)'),
    ("offset_zero", 'm.offset_for_focal(0.0, 10.0) == approx(0.0)'),
    ("order", 'm.apply_order("distort", "aberration") == ("distort", "aberration")'),
    ("clamp_high", 'm.clamp_uv(1.5) == approx(1.0)'),
    ("clamp_low", 'm.clamp_uv(-0.5) == approx(0.0)'),
    ("luma", 'm.luma_weight(1.0) == approx(0.5)'),
    ("ui_true", 'm.exclude_ui("ui") is True'),
    ("ui_false", 'm.exclude_ui("scene") is False'),
    ("scale", 'm.scale_radius(0.1, 1920, 960) == approx(0.2)'),
    ("temporal", 'm.temporal_scale(0.5, 1.0) == approx(0.5)'),
    ("channel_r", 'm.channel_offset("r", 0.1) == approx(0.1)'),
    ("channel_g", 'm.channel_offset("g", 0.1) == approx(0.0)'),
    ("animate", 'm.animate_param(2.0, 0.5) == approx(1.0)'),
    ("half", 'm.half_float_clamp(70000.0) == approx(65504.0)')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
