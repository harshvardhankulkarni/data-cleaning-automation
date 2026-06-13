# Architecture: Data Cleaning Automation

## Context

Real-world data is never clean. CRM exports, spreadsheets, and database dumps all have quality issues. Before any analysis can happen, the data must be cleaned. Automating this process saves hours of manual work and prevents bad decisions.

## Goals

- Detect common data quality issues automatically.
- Apply standardized fixes to each issue type.
- Produce a before/after quality report.
- Export clean data for downstream analysis.

## Design

### Data Flow

```
Dirty Data Generator
  - 150 records with controlled errors
  - 9 columns with different issue types
        |
        v
Data Quality Scanner
  - Null count per column
  - Empty string count
  - Duplicate detection
        |
        v
Cleaning Pipeline (10 steps, sequential)
  Step 1:  Drop duplicates
  Step 2:  Clean names (strip, capitalize, remove newlines)
  Step 3:  Validate email format
  Step 4:  Standardize city names (lookup mapping)
  Step 5:  Normalize categories
  Step 6:  Fix negative spend (absolute value)
  Step 7:  Parse dates (multiple format fallback)
  Step 8:  Standardize active flag
  Step 9:  Flag missing phones
  Step 10: Generate quality report
        |
        v
Clean DataFrame --> Visualization + CSV Export
```

### Cleaning Function Pattern

Each cleaning operation follows the same pattern:

```python
def clean_column(val):
    if pd.isna(val):
        return default_value
    val = str(val).strip()
    # transformation logic
    return val

df['column'] = df['column'].apply(clean_column)
```

### Data Quality Scoring

The report compares before and after:

- Total rows before/after.
- Null count per column.
- Duplicate count.
- Issues found and fixed count.

## Key Decisions

| Decision | Rationale |
|----------|-----------|
| Apply functions instead of regex | More readable. Easier to debug. Handles edge cases better. |
| Sequential pipeline | Each step depends on the previous. Order matters (clean names before validating emails). |
| Lookup dictionary for cities | Explicit mapping is safer than fuzzy matching for known values. |
| Absolute value for negative spend | Assumes sign error (data entry mistake). Logs the count for review. |

## Trade-offs

- **Apply functions vs vectorized operations**: Apply is slower on large datasets (1M+ rows) but more readable. Vectorized cleaning would need more complex logic.
- **Hardcoded mappings vs ML**: City name standardization uses a fixed dictionary. For unknown cities, it falls back to the original value. A fuzzy matching library (fuzzywuzzy) would catch more variants but add a dependency.
- **Destructive vs non-destructive**: The pipeline modifies data in place. A production version should keep an audit trail of original values.

## Integration Points

- **Input**: Self generates data. Replace with `pd.read_csv('export.csv')`.
- **Output**: `cleaned_data_output.csv` is ready for analysis, dashboarding, or CRM import.
- **Extending**: Add new cleaning functions for new column types. Each function is independent.

## Dependencies

- Python 3.8+
- pandas, numpy, matplotlib
