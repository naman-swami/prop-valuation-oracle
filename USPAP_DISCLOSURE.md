# Uniform Standards of Professional Appraisal Practice (USPAP) Disclosure

## 1. Appraisal Standards Board (ASB) Compliance
Prop Valuation Oracle models real estate asset valuations in accordance with:
- **The Uniform Standards of Professional Appraisal Practice (USPAP 2024–2025 Edition)**
- **Financial Institutions Reform, Recovery, and Enforcement Act of 1989 (FIRREA Title XI)**
- **Interagency Appraisal and Evaluation Guidelines (OCC, FRB, FDIC, NCUA)**

---

## 2. Valuation Methodologies & Formulations

### A. Sales Comparison Approach (Hedonic Econometric Pricing)
Models fair market value by comparing the subject property with verified recent sales of comparable properties ("comps") within the same geographic sub-market:

$$\ln(\text{Price}) = \beta_0 + \beta_1 \cdot \text{GLA} + \beta_2 \cdot \text{Bedrooms} + \beta_3 \cdot \text{Bathrooms} + \beta_4 \cdot \text{Age} + \sum \gamma_k Z_k + \epsilon$$

Where $\text{GLA}$ is Gross Living Area ($	ext{sq ft}$) and $Z_k$ represents localized neighborhood amenities and school district ratings.

### Comp Adjustment Thresholds:
- **Net Adjustments**: Total dollar net adjustment on any comp should not exceed **15%** of the comp's sale price.
- **Gross Adjustments**: Total dollar gross adjustment should not exceed **25%** of the comp's sale price.

### B. Income Capitalization Approach (Commercial Multifamily & Retail)
Derives property valuation from stabilized Net Operating Income ($NOI$):

$$V = \frac{\text{Net Operating Income (NOI)}}{R_{\text{cap}}}$$

Where:
- $NOI = \text{Effective Gross Income (EGI)} - \text{Operating Expenses (OPEX)}$.
- $R_{\text{cap}}$: Prevailing market capitalization rate for the specific commercial asset tier ($4.5\% - 7.5\%$).

---

## 3. Appraiser Certification & Ethical Independence
- **USPAP Ethics Rule**: The valuation engine operates with complete independence. Model valuations are never conditioned on a predetermined value or loan approval outcome.
- **Limiting Conditions**: Valuations assume marketable title and absence of hidden environmental hazards or structural foundation defects.
