import pytest
from src.valuation_engine import PropertyValuationEngine

def test_valuation_scale():
    engine = PropertyValuationEngine()
    val = engine.estimate_property_value(2000, 3, 2.0, 5, 8.0)
    assert val["estimated_valuation_usd"] > 500000

def test_cap_rate():
    engine = PropertyValuationEngine()
    cap = engine.compute_cap_rate(1000000, 100000, operating_expense_ratio=0.40)
    # NOI = 60,000 / 1,000,000 = 6.0%
    assert cap["cap_rate_pct"] == 6.0
