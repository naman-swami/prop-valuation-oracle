# Prop Valuation Oracle & Hedonic Appraisal Engine

[![OpenGAP](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](agent.yaml)
[![PropTech](https://img.shields.io/badge/Domain-Real_Estate_Appraisal-gold.svg)](docs/uspap_appraisal_standards.md)
[![Standard](https://img.shields.io/badge/Standard-USPAP_Appraisal-blue.svg)](docs/uspap_appraisal_standards.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](requirements.txt)
[![CI](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/ci.yml)

An institutional real estate appraisal and automated valuation model (AVM) engine computing hedonic property adjustments, Net Operating Income (NOI), and capitalization rates.

```
                    ┌─────────────────────────┐
                    │ Property Physical Specs │
                    │ (SqFt, Beds, Year, Rent)│
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ models/hedonic_pricing  │
                    └────────────┬────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
      ┌─────────────────────┐         ┌─────────────────────┐
      │  Hedonic Value USD  │         │  Cap Rate (NOI/Val) │
      │  (Comp Adjustments) │         │ (Cash Flow Yield)   │
      └──────────┬──────────┘         └──────────┬──────────┘
                 │                               │
                 └───────────────┬───────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │ Investment Rating Plan  │
                    │ (PRIME_CASH_FLOW / YIELD│
                    └─────────────────────────┘
```

## Features

- **Hedonic Appraisal Adjustments**: Accounts for square footage, bedroom configuration, and building depreciation.
- **Cap Rate Yield Analysis**: Accurately computes un-leveraged property yields from net operating income.
- **Comps Grounding**: Includes benchmark residential real estate sales and rent registers.

## Directory Structure

```
prop-valuation-oracle/
├── agent.yaml                       # OpenGAP 0.1.0 Manifest
├── EXPLAINABILITY.md                # 7-checkpoint real estate provenance
├── models/
│   └── hedonic_pricing_model.py     # Hedonic pricing & cap rate engine
├── fixtures/
│   └── comps/
│       └── sample_market_comps.json # Benchmark comparable sales
├── docs/
│   └── uspap_appraisal_standards.md # Real estate appraisal standards
├── tests/
│   └── test_agent.py                # Valuation test suite
├── main.py                          # PropTech CLI
└── requirements.txt
```

## Quick Start

```bash
# Run real estate valuation tests
pytest tests/ -v

# Appraise sample market comps
python main.py --demo
```
