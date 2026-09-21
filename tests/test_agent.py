import os
import pytest
from models.hedonic_pricing_model import RealEstateValuationEngine

def test_valuation_and_cap_rate():
    res = RealEstateValuationEngine.calculate_valuation_and_cap_rate(
        sqft=2000, base_price_per_sqft=300.0, bedrooms=3, year_built=2025,
        gross_rent=40000.0, operating_expenses=10000.0
    )
    assert res["estimated_property_value_usd"] == 600000.0
    assert res["net_operating_income_usd"] == 30000.0
    assert res["capitalization_rate_pct"] == 5.0
    assert res["investment_rating"] == "CORE_STABILIZED"
