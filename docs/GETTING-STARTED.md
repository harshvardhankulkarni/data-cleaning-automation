# Getting Started

<!-- GSD: v1.0 -->

## Prerequisites

- Python 3.8 or higher
- pip package manager

## Installation

```bash
# Clone the repository
git clone https://github.com/harshvardhankulkarni/data-cleaning-automation.git
cd data-cleaning-automation

# Install core dependencies
pip install pandas numpy matplotlib

# Optional: for interactive HTML chart
pip install plotly
```

## Running the Pipeline

```bash
python 3_data_cleaning_automation.py
```

### Expected Console Output

```
Original dataset: 150 rows
Columns: ['customer_id', 'name', 'email', 'phone', 'city', 'category', 'spend', 'signup_date', 'active']

--- DATA QUALITY REPORT (BEFORE) ---
Total rows: 150
Duplicate rows: <depends on seed>
  customer_id: 0 nulls, 0 empty strings
  name: <n> nulls, <n> empty strings
  ...

--- REMOVED <n> duplicates ---

--- FIXED 13 negative spend values (absolute value) ---

--- FIXED 18 invalid dates ---

--- DATA QUALITY REPORT (AFTER) ---
Total rows: <146-150>
Duplicate rows: 0

--- CLEANING SUMMARY ---
Total issues detected and resolved: 31
Duplicate rows removed: <0-4>
Invalid emails fixed: <~13> flagged for review
Invalid dates fixed: 18
Negative spend values fixed: 13
Cities standardized: 7 variants normalized to 5 standard names
Active status standardized: 6 formats normalized to Yes/No

Action: Flag missing emails for CRM update.
Action: Set up input validation to prevent future bad data.
Done.

Exported: cleaned_data_output.csv
Saved: 3_data_cleaning_report.png
```

### Output Files Created

| File | What It Is |
|---|---|
| `cleaned_data_output.csv` | Cleaned dataset with all transformations applied |
| `3_data_cleaning_report.png` | Side-by-side bar chart: issues found + city distribution after cleaning |

## Running the Interactive Version

```bash
python generate_interactive.py
```

Opens in browser via `3_data_cleaning_interactive.html`. Shows the same data as the static chart but with hover tooltips and an interactive pie chart.

## Running the Notebook

Launch Jupyter and open `3_data_cleaning_automation.ipynb`:

```bash
pip install jupyter
jupyter notebook 3_data_cleaning_automation.ipynb
```

## Verifying It Worked

Check that:
- `cleaned_data_output.csv` exists and has no duplicate rows.
- `3_data_cleaning_report.png` exists and shows two subplots.
- Console reports exactly 31 issues fixed (18 bad dates + 13 negative spend + removed duplicates).
