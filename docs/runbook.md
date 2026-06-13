# Runbook: Data Cleaning Automation

## When to Use This Runbook

- Running the cleaning pipeline for the first time.
- Adapting the pipeline for a new dataset.
- Debugging cleaning errors.

## Prerequisites

- Python 3.8+ installed.
- pip installed.
- Source CSV file with similar structure (optional).

## Procedure

### Step 1: Install Dependencies

```bash
pip install pandas numpy matplotlib
```

### Step 2: Run the Default Pipeline

```bash
cd path/to/data-cleaning-automation
python 3_data_cleaning_automation.py
```

### Step 3: Verify the Output

Check these files:

- `3_data_cleaning_report.png` - Shows issues found and cleaned distribution.
- `cleaned_data_output.csv` - All 150 records cleaned. No null categories. No negative spend. All dates valid.

### Step 4: Run with Real Data

Replace the data generation block (lines 15-38) with:

```python
df = pd.read_csv('your_crm_export.csv')
```

Remove or adjust seed for non-random data.

### Step 5: Interpret the Quality Report

The console output shows two reports:

**Before**: Raw counts of nulls and empty strings per column.

**After**: Remaining issues (some missing data is expected, like phone numbers).

The cleaning summary tells you exactly how many issues were found and fixed.

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| OverflowError | Random number too large for int32 | Use Python random module instead of numpy for phone numbers |
| No date parsed | Date format not in the list | Add your format to the `formats` list |
| City not recognized | Not in lookup dictionary | Add it to `city_map` or use fuzzy matching |
| Column not found | Real CSV has different column names | Map column names in the read step |
| Slow on large dataset | Apply functions on 100K+ rows | Use vectorized `str.replace()` instead of apply |

## Adapting for Your Data

### Step 1: Map Your Columns

Create a mapping from your column names to the expected names:

```python
column_map = {
    'Full Name': 'name',
    'Email Address': 'email',
    'Mobile': 'phone',
    'Location': 'city',
}
df = df.rename(columns=column_map)
```

### Step 2: Add Missing Cleaning Rules

Add new cleaning functions after the existing ones:

```python
def clean_pincode(val):
    if pd.isna(val):
        return None
    val = str(val).strip()
    return val[:6]  # Keep first 6 digits

df['pincode'] = df['pincode'].apply(clean_pincode)
```

### Step 3: Disable Steps You Don't Need

Comment out cleaning steps that do not apply to your data.

## Escalation

Open a GitHub issue with:

- Sample of your raw data (5-10 rows, anonymized).
- Error message if any.
- Expected output.
- Python version and operating system.
