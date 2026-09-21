import argparse
import json
import os
from models.hedonic_pricing_model import RealEstateValuationEngine

def main():
    parser = argparse.ArgumentParser(description="Prop Valuation Oracle CLI")
    parser.add_argument("--demo", action="store_true", help="Appraise sample real estate comps")
    args = parser.parse_args()

    data_file = os.path.join(os.path.dirname(__file__), "fixtures", "comps", "sample_market_comps.json")

    if args.demo:
        with open(data_file, "r") as f:
            comps = json.load(f)
        print("=== PROP VALUATION ORACLE APPRAISAL REPORT ===\n")
        for c in comps:
            res = RealEstateValuationEngine.calculate_valuation_and_cap_rate(
                sqft=c["sqft"],
                base_price_per_sqft=310.0,
                bedrooms=c["bedrooms"],
                year_built=c["year_built"],
                gross_rent=c["annual_gross_rent"],
                operating_expenses=c["operating_expenses"]
            )
            print(f"Property [{c['comp_id']}] {c['sqft']} sqft | Built: {c['year_built']}")
            print(f"  Estimated Valuation: ${res['estimated_property_value_usd']:,.2f}")
            print(f"  NOI: ${res['net_operating_income_usd']:,.2f} | Cap Rate: {res['capitalization_rate_pct']}%")
            print(f"  Investment Tier: {res['investment_rating']}")
            print("-" * 50)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
