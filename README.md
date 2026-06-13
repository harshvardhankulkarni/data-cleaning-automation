# Data Cleaning Automation - Demo Project

End-to-end data cleaning pipeline for real-world messy data. Simulates a dirty CRM export and fixes it step by step.

This is a demo project using synthetic data to demonstrate data quality and cleaning techniques.

## Tech Stack

- Python 3.8+
- Pandas 2.0+ - Data manipulation and cleaning
- NumPy 1.24+ - Random data generation
- Matplotlib 3.7+ - Visualization

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

```bash
git clone https://github.com/harshvardhankulkarni/data-cleaning-automation.git
cd data-cleaning-automation
pip install pandas numpy matplotlib
```

### Running

```bash
python 3_data_cleaning_automation.py
```

Expected output:

```
Original dataset: 150 rows
--- DATA QUALITY REPORT (BEFORE) ---
--- FIXED 13 negative spend values ---
--- FIXED 18 invalid dates ---
--- CLEANING SUMMARY ---
Total issues detected and resolved: 31
...
Exported: cleaned_data_output.csv
Done.
```

### Output Files

| File | Description |
|------|-------------|
| 3_data_cleaning_report.png | Before/after comparison chart |
| cleaned_data_output.csv | Cleaned dataset with all fixes applied |

## How It Works

The script generates a deliberately dirty dataset (150 records, 9 columns) with these issues:

| Column | Issues Introduced | Frequency |
|--------|------------------|-----------|
| name | Empty strings, leading/trailing spaces, newlines, None | 22% |
| email | Missing "@", empty strings | 10% |
| phone | "NOT_AVAILABLE" placeholder | 15% |
| city | Different cases, misspellings ("PUNE", "mumbai", "Bngalore") | 20%+ |
| category | NaN values | 12% |
| spend | Negative values (data entry errors) | 8% |
| signup_date | Invalid dates ("not_a_date"), month 13 | 12% |
| active | 6 formats ("Yes", "Y", "TRUE", "No", "N", "FALSE", None) | 26% |

### Cleaning Steps Applied

1. Remove duplicate rows.
2. Strip whitespace and capitalize names.
3. Validate email format (must contain "@" with domain).
4. Standardize city names using a lookup dictionary.
5. Normalize product categories.
6. Fix negative spend by taking absolute value.
7. Parse dates using multiple format fallbacks.
8. Standardize active flag to "Yes" or "No".
9. Flag missing phones for CRM update.
10. Generate before/after data quality report.

## Project Structure

```
data-cleaning-automation/
  3_data_cleaning_automation.py   Main cleaning script
  README.md                       This file
  docs/
    architecture.md                Design and methodology
    runbook.md                     Operations guide
```

## Configuration

- `np.random.seed(42)` - Change for different data.
- `n = 150` - Number of records to generate.
- Error rates are controlled by `np.random.random() > threshold` checks.
- City mapping dictionary in `clean_city()` function.

## Extending

Add new cleaning rules by following the existing pattern:

1. Create a new `clean_*` function.
2. Apply it to the DataFrame column.
3. Update the data quality report.

## License

MIT
