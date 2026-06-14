# Data Cleaning Automation

<!-- GSD: v1.0 -->

End-to-end data cleaning pipeline for CRM-style data. Generates a deliberately dirty synthetic dataset (150 records, 9 columns) with 9 categories of real-world data quality issues, then applies 10 sequential cleaning transformations. Produces before/after quality reports and exports clean data.

## Issue Categories Detected

| Category | Example | Frequency |
|---|---|---|
| Duplicate records | `'Rahul Sharma'` appears twice in `names` pool | ~random |
| Empty strings in text fields | `''` in name, `''` in email, `''` in active | varies |
| Missing `@` in email | `'user45email.com'` | ~5% |
| Whitespace / newline artifacts | `'  Sneha Kapoor  '`, `'Ananya Gupta\n'` | ~10% |
| Null/NaN values | `np.nan` in category, city, name, active | ~12-18% |
| Invalid dates | `'2024/13/01'` (month 13), `'not_a_date'` | ~12% |
| Negative spend values | `-round(np.random.exponential(5000), 2)` | ~8% |
| Inconsistent casing / misspellings | `'PUNE'`, `'mumbai'`, `'Bngalore'` | ~20%+ |
| Placeholder values | `'NOT_AVAILABLE'` for phone | ~15% |
| Non-standardized boolean flags | 6 formats: `Yes/No/Y/N/TRUE/FALSE` + empty + None | ~26% |

## Cleaning Steps (in order)

| Step | Operation | Details |
|---|---|---|
| 1 | Profile before cleaning | Count nulls, empty strings, duplicates per column |
| 2 | Remove duplicate rows | `df.drop_duplicates()` |
| 3 | Clean names | Strip whitespace, remove `\n`/`\r`, capitalize each part |
| 4 | Fix email format | Validate `@` and domain (`.` in domain part); set to None if invalid |
| 5 | Standardize city names | 19-entry lookup dict: `'pune'→'Pune'`, `'bngalore'→'Bangalore'`, etc. |
| 6 | Clean categories | `NaN→'Uncategorized'`, `'Home'→'Home & Kitchen'`, `'Sports'→'Sports & Fitness'` |
| 7 | Fix negative spend | `abs()` — logs count for audit |
| 8 | Parse and validate dates | 4 format fallback: `%Y-%m-%d`, `%d-%m-%Y`, `%m/%d/%Y`, `%Y/%m/%d` |
| 9 | Standardize active flag | `Yes/Y/TRUE/1/active→'Yes'`, everything else→`'No'` |
| 10 | Replace unknown phones | `'NOT_AVAILABLE'`→`None` |

## Tech Stack

- **Python 3.8+** — Core language
- **Pandas 2.0+** — Data manipulation and cleaning
- **NumPy 1.24+** — Random data generation
- **Matplotlib 3.7+** — Before/after visualization (PNG)
- **Plotly 5.x** — Interactive HTML chart (optional, separate script)

## Quick Start

```bash
pip install pandas numpy matplotlib
python 3_data_cleaning_automation.py
```

Expected output:
```
Original dataset: 150 rows
--- FIXED 13 negative spend values ---
--- FIXED 18 invalid dates ---
--- CLEANING SUMMARY ---
Total issues detected and resolved: 31
Exported: cleaned_data_output.csv
```

### Output Files

| File | Description |
|---|---|
| `cleaned_data_output.csv` | Cleaned dataset (all fixes applied) |
| `3_data_cleaning_report.png` | Before/after comparison chart |
| `3_data_cleaning_interactive.html` | Plotly interactive report (run `generate_interactive.py`) |

## Project Structure

```
data-cleaning-automation/
  3_data_cleaning_automation.py   Main cleaning script
  3_data_cleaning_automation.ipynb Jupyter notebook
  generate_interactive.py          Plotly interactive chart generator
  cleaned_data_output.csv          Generated clean dataset
  3_data_cleaning_report.png       Before/after chart
  3_data_cleaning_interactive.html Interactive chart
  index.html                       GitHub Pages site
  README.md                        This file
  docs/
    ARCHITECTURE.md                Design and methodology
    GETTING-STARTED.md             Setup and run instructions
    DEVELOPMENT.md                 Extension guide
    TESTING.md                     Manual validation procedures
    CONFIGURATION.md               Parameter reference
```

## Demo

This is a demo / portfolio project. The dataset is synthetic. See the [live GitHub Pages site](https://harshvardhankulkarni.github.io/data-cleaning-automation/) for the interactive chart.
