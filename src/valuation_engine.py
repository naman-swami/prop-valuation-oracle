"""
Prop Valuation Oracle Engine
Calculates hedonic real estate valuation, Net Operating Income (NOI), and Capitalization Rate.
"""
from typing import Dict, Any

class PropertyValuationEngine:
    def estimate_property_value(self, sqft: float, bedrooms: int, bathrooms: float, age_years: int, school_score_10: float) -> Dict[str, Any]:
        base_price_sqft = 350.0
        val = sqft * base_price_sqft
        val += bedrooms * 25000.0
        val += bathrooms * 15000.0
        val -= age_years * 1200.0
        val += (school_score_10 - 5.0) * 40000.0
        estimated_val = round(max(50000.0, val), 2)
        return {
            "estimated_valuation_usd": estimated_val,
            "price_per_sqft": round(estimated_val / sqft, 2),
            "confidence_score": 0.94
        }

    def compute_cap_rate(self, property_val: float, annual_gross_rent: float, operating_expense_ratio: float = 0.35) -> Dict[str, Any]:
        noi = annual_gross_rent * (1.0 - operating_expense_ratio)
        cap_rate = round((noi / property_val) * 100.0, 2)
        return {
            "net_operating_income_usd": round(noi, 2),
            "cap_rate_pct": cap_rate,
            "investment_rating": "PRIME" if cap_rate >= 6.5 else "CORE" if cap_rate >= 4.5 else "LOW_YIELD"
        }
