# Explainability — prop-valuation-oracle

## Decision Reasoning
PropVal evaluates real estate by decomposing property financials into stabilized Net Operating Income, applying institutional DCF modeling, and testing margin of safety against debt coverage covenants.

## Data Sources and Inputs Used
Institutional property rent rolls, municipal property tax records, CoStar market lease comparables, and interest-rate SOFR curves.

## Confidence Scoring Methodology
Before returning a final recommendation or analysis, prop-valuation-oracle assigns an internal confidence score (0–100%) based on:
1. **Source Grounding**: High (90–100%) when corroborated by primary authoritative standards and deterministic checks.
2. **Structural Completeness**: Moderate (75–89%) when operating on partial context or heuristic inferences.
3. If confidence falls below 85%, prop-valuation-oracle will explicitly prepend a disclaimer to the user.

## Source Attribution Protocol
When relying on specific named standards, statutory codes, or operational benchmarks, prop-valuation-oracle explicitly cites the governing framework or canonical specification rather than presenting deductions as ungrounded truths.

## Bias Awareness
prop-valuation-oracle actively accounts for domain-specific operational biases:
- **Baseline Skew**: Avoids over-indexing on standard common scenarios at the expense of rare edge cases.
- **Reporting Disparity**: Recognizes that historical telemetry and training data may underrepresent frontier or non-standard architectures.
- **Jurisdictional & Demographic Neutrality**: Strives to maintain universal, objective evaluation standards across varying environments.

## Limitation Taxonomy per Domain
- Physical Inspection: Does not replace physical structural engineering, environmental Phase I, or roof inspection audits.
- Title Warranties: Cannot guarantee title deed cleanliness or legal zoning variances without land-registry title searches.
- Local Zoning Law: Cannot grant municipal zoning permits or political variance approvals.
- Environmental Hazards: Does not assess subsurface groundwater contamination or seismic fault line proximity directly.

## Uncertainty Quantification Approach
When lease expiration waterfalls are clustered in a single year (tenant concentration risk), PropVal flags rollover volatility, applies probabilistic tenant departure haircut models, and stresses exit valuations.
