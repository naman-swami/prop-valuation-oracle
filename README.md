# Prop Valuation Oracle & Appraisal Engine

> **Real Estate Hedonic Regression & Commercial Income Capitalization Oracle**  
> Conforming to the Uniform Standards of Professional Appraisal Practice (USPAP).

---

### Valuation Methodologies

#### 1. Hedonic Price Model (Residential Sales Comparison)
Estimates property value based on physical attributes and localized market premiums:

$$\ln(\text{Price}) = \beta_0 + \beta_1 \cdot \text{SqFt} + \beta_2 \cdot \text{Beds} + \beta_3 \cdot \text{Baths} + \beta_4 \cdot \text{Age} + \epsilon$$

#### 2. Income Capitalization Approach (Commercial Property)
Calculates present asset value from Net Operating Income ($NOI$):

$$V = \frac{\text{Net Operating Income (NOI)}}{\text{Market Capitalization Rate } (R_{cap})}$$

---

### Sample Property Appraisal Breakdown

Evaluated for subject property (`fixtures/comps/sample_market_comps.json`):

```console
$ python val_oracle.py --demo
======================================================================
USPAP APPRAISAL VALUATION MEMORANDUM: 742 Evergreen Terrace
Property Class: Single Family Residential | Gross Living Area: 2,400 sqft
======================================================================
* Base Hedonic Estimate:       $585,000.00
* Comparable #1 Adjustment:    +$15,000.00 (Recent bathroom renovation)
* Comparable #2 Adjustment:    -$8,500.00  (Lot size differential)
* Final Reconciled Valuation:  $591,500.00 USD
* 90% Confidence Interval:     [$573,000.00 - $610,000.00]
======================================================================
Appraisal Status: USPAP COMPLIANT RECONCILIATION
```

---

### Valuation CLI Execution

```bash
# Run appraisal valuation against market comps
python val_oracle.py --demo

# Verify econometric valuation test suite
pytest tests/ -v
```

Appraisal ethics, market comp selection guidelines, and certification disclosures are published in [USPAP_DISCLOSURE.md](USPAP_DISCLOSURE.md).
