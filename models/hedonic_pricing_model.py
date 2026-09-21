"""
PropTech Hedonic Appraisal & Capitalization Rate (Cap Rate) Engine
Calculates hedonic valuation adjustments and Net Operating Income (NOI) capitalization yields.
"""
from typing import Dict, Any

class RealEstateValuationEngine:
    @staticmethod
    def calculate_valuation_and_cap_rate(
        sqft: int,
        base_price_per_sqft: float,
        bedrooms: int,
        year_built: int,
        gross_rent: float,
        operating_expenses: float
    ) -> Dict[str, Any]:
        # Hedonic base estimate
        base_val = sqft * base_price_per_sqft
        bed_adj = (bedrooms - 3) * 15000.0
        age_deprec = max(0, 2025 - year_built) * 750.0
        estimated_value = round(base_val + bed_adj - age_deprec, 2)

        # Net Operating Income (NOI)
        noi = round(gross_rent - operating_expenses, 2)
        cap_rate_pct = round((noi / max(1.0, estimated_value)) * 100, 2)

        investment_tier = "PRIME_CASH_FLOW" if cap_rate_pct >= 6.5 else "CORE_STABILIZED" if cap_rate_pct >= 4.5 else "LOW_YIELD_APPRECIATION"

        return {
            "estimated_property_value_usd": estimated_value,
            "net_operating_income_usd": noi,
            "capitalization_rate_pct": cap_rate_pct,
            "investment_rating": investment_tier
        }
