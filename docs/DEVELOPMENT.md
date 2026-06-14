# Development Guide

<!-- GSD: v1.0 -->

## Project Structure

```
data-cleaning-automation/
  3_data_cleaning_automation.py    Main pipeline (dirty gen + 10 cleaning steps + report)
  3_data_cleaning_automation.ipynb Jupyter notebook (same logic with markdown cells)
  generate_interactive.py          Standalone Plotly chart (bar + pie)
  index.html                       GitHub Pages landing page (dark theme)
  cleaned_data_output.csv          Generated output (ignore in git)
  3_data_cleaning_report.png       Generated chart (ignore in git)
  3_data_cleaning_interactive.html Generated interactive chart (ignore in git)
  docs/                            Documentation
```

## Code Conventions

- **Functions**: Each cleaning step is a `clean_<column>()` function taking a single value, applied via `df['col'].apply(clean_col)`.
- **Naming**: `snake_case` for functions and variables. `UPPER_CASE` for constants.
- **Side effects**: Print statements for pipeline progress. No logging library.
- **Seed**: `np.random.seed(42)` at the top of the script for deterministic data generation.

## How to Add a New Cleaning Rule

1. Create a new cleaning function following the existing pattern:

```python
def clean_new_column(val):
    if pd.isna(val):
        return default_value           # handle nulls first
    val = str(val).strip().lower()     # normalize
    # transformation logic
    return result
```

2. Apply it to the DataFrame column:

```python
df['new_column'] = df['new_column'].apply(clean_new_column)
```

3. Add a print statement to report how many values were changed:

```python
print(f'--- FIXED {count} new_column issues ---')
```

4. Update the cleaning summary section at the bottom of the script to include the new count.

## How to Modify an Existing Transformation

Locate the `clean_*` function for the column you need to modify in `3_data_cleaning_automation.py`. Each function follows this structure:

- Null/NaN guard at the top.
- String normalization (`strip()`, `lower()`).
- Core transformation logic (dict lookup, regex, conditional).
- Return the cleaned value.

For example, to add a new city variant to the city mapper:

```python
city_map = {
    # ... existing entries ...
    'surat': 'Surat',           # add new mapping
    'ahmedabad': 'Ahmedabad',   # add new mapping
}
```

## Adding New Issue Types to the Dirty Data Generator

1. Add a new column to the `data` dictionary in the dirty data generation section (around line 25).
2. Seed it with deliberate errors (wrong types, missing values, invalid formats).
3. Create a corresponding `clean_*` function.
4. Add it to the pipeline between the existing steps (order may matter).
5. Add the new column to the profiling loop if you want it in the before/after report.

## Code Style

- Follow PEP 8.
- Keep functions short (under 20 lines).
- Prefer `apply()` with named functions over lambdas for readability.
- Document each cleaning step with a comment header.
- Print progress at each step so the user can trace execution.
