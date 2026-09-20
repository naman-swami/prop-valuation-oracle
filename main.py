import json
import argparse
from src.valuation_engine import PropertyValuationEngine

def main():
    parser = argparse.ArgumentParser(description="Prop Valuation Oracle CLI")
    parser.add_argument("--demo", action="store_true", help="Run simulated residential asset appraisal")
    args = parser.parse_args()

    engine = PropertyValuationEngine()
    appraisal = engine.estimate_property_value(sqft=2400, bedrooms=4, bathrooms=3.0, age_years=8, school_score_10=8.5)
    cap = engine.compute_cap_rate(appraisal["estimated_valuation_usd"], annual_gross_rent=72000)

    report = {"appraisal": appraisal, "investment_yield": cap}
    print("="*60)
    print(" PROP VALUATION ORACLE REAL ESTATE AUDIT REPORT")
    print("="*60)
    print(json.dumps(report, indent=2))
    print("="*60)

if __name__ == "__main__":
    main()
