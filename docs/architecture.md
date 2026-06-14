<!-- GSD -->

# Data Cleaning Automation — Architecture

## Context and Goals

End-to-end data cleaning pipeline that generates a deliberately dirty dataset (150 records) with 9 categories of data quality issues, then applies 10 step-by-step cleaning transformations. Portfolio demo showcasing data quality workflows.

## Data Flow

```
Dirty Data Generation (seed=42, 150 records)
  → 9 issue types injected (dupes, bad emails, invalid dates, negative spend, inconsistent casing, missing values)
  → 10 step cleaning pipeline
  → Before/after quality comparison
  → Static matplotlib report chart
  → Interactive Plotly issue distribution
  → Clean CSV export (31 issues fixed)
```

## Components

| File | Role |
|------|------|
| `3_data_cleaning_automation.py` | Main pipeline: dirty data generation, 10 cleaning steps, quality report, CSV export |
| `generate_interactive.py` | Generates interactive Plotly HTML version showing issue distribution |
| `3_data_cleaning_automation.ipynb` | Jupyter notebook for exploratory development |
| `cleaned_data_output.csv` | Cleaned dataset output |
| `3_data_cleaning_report.png` | Before/after comparison chart |
| `3_data_cleaning_interactive.html` | Interactive Plotly chart |

## Cleaning Steps

1. Remove duplicate records
2. Standardize name casing
3. Validate email formats
4. Standardize city names
5. Normalize category values
6. Clean spend column (remove negatives)
7. Standardize date formats
8. Clean active flag
9. Format phone numbers
10. Final validation pass

## Design Decisions

| Decision | Rationale |
|----------|-----------|
| seed=42 | Reproducible dirty data generation |
| 150 records | Enough to demonstrate variety of issues without large data |
| 9 issue categories | Covers common CRM data quality problems |
| 10 sequential steps | Logical pipeline order: identity → text → numeric → date → validation |
| 31 total issues | Measurable quality improvement metric |

## Trade-offs

- Synthetic data has known issues — real data often has unexpected quality problems
- Sequential pipeline means later steps depend on earlier ones
- Rule-based cleaning only — no ML-based anomaly detection
- Limited to structured tabular data

## File Organization

```
data-cleaning-automation/
├── 3_data_cleaning_automation.py
├── generate_interactive.py
├── 3_data_cleaning_automation.ipynb
├── 3_data_cleaning_report.png
├── 3_data_cleaning_interactive.html
├── cleaned_data_output.csv
├── index.html
└── docs/
    ├── ARCHITECTURE.md
    ├── GETTING-STARTED.md
    ├── DEVELOPMENT.md
    ├── TESTING.md
    └── CONFIGURATION.md
```
