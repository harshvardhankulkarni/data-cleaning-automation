# Data Cleaning Automation

End-to-end data cleaning pipeline for real-world messy data. Simulates a dirty CRM export and fixes it step by step.

## Problem

Real data is never clean. CRM exports have duplicates, invalid emails, inconsistent city names, non-standardized flags, bad dates, negative values, and missing fields. Every analysis project starts with cleaning. Automating this step saves hours and prevents bad decisions.

## Approach

Generated a deliberately dirty dataset with 150 records and 9 columns. Each column has a different type of data quality issue:

| Issue | Example | Frequency |
|-------|---------|-----------|
| Empty names | "", "None" | 22% |
| Invalid emails | Missing @, wrong domain | 8% |
| Missing phones | "NOT_AVAILABLE" | 15% |
| Inconsistent cities | "PUNE", "mumbai", "Bngalore" | 20% |
| Null categories | NaN | 12% |
| Negative spend | -Rs.4,532 | 8% |
| Bad dates | "not_a_date", month 13 | 12% |
| Non-standard flags | "Y", "TRUE", "Yes", "N" | 26% |

Applied 10 cleaning steps:
1. Remove duplicates
2. Strip and capitalize names
3. Validate email format
4. Standardize city names using lookup mapping
5. Normalize product categories
6. Fix negative spend values (take absolute)
7. Parse dates with multiple format fallback
8. Standardize active flag to Yes/No
9. Flag missing phones for CRM update
10. Generate data quality report

## Results

- 31 total issues detected and resolved.
- City names normalized from 7 variants to 5 standard names.
- Active status unified from 6 formats to Yes/No.
- Bad emails and dates flagged for manual review.
- Full before-and-after comparison chart saved.

## How to Run

```bash
pip install pandas matplotlib numpy
python 3_data_cleaning_automation.py
```

Output: `3_data_cleaning_report.png` (chart) and `cleaned_data_output.csv` (clean data).

## Tech Stack

Python, Pandas, NumPy, Matplotlib

## License

MIT
