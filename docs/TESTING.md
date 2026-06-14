# Testing

<!-- GSD: v1.0 -->

## Test Status

**No automated test suite.** The project uses manual validation only. This is acceptable for a demo/portfolio project. For production use, add pytest tests for each `clean_*` function.

## Manual Validation Procedure

Run the pipeline with seed `42` and verify the following:

### 1. Console Output Checks

| Check | Expected | How to Verify |
|---|---|---|
| Total rows before cleaning | 150 | First line of output |
| Total issues detected and resolved | 31 | Summary section (`invalid_dates + neg_spend + duplicates_removed`) |
| Invalid dates fixed | 18 | `--- FIXED 18 invalid dates ---` |
| Negative spend values fixed | 13 | `--- FIXED 13 negative spend values ---` |
| Empty rows after cleaning | 0 | Final profile shows no null/empty counts |
| Duplicate rows after cleaning | 0 | `Duplicate rows: 0` in after report |

### 2. Issue Counts by Category

The deterministic seed (`42`) should produce consistent counts:

- **Bad emails flagged**: approx 13 (emails set to `None` by validation)
- **Bad dates fixed**: 18
- **Negative spend fixed**: 13
- **Cities standardized**: 7 variants → 5 standard names
- **Active status formats normalized**: 6 formats → `Yes`/`No`

### 3. Output File Existence

| File | Must Exist |
|---|---|
| `cleaned_data_output.csv` | Yes — non-empty, valid CSV |
| `3_data_cleaning_report.png` | Yes — renders 2 subplots |

### 4. CSV Content Validation

Open `cleaned_data_output.csv` and verify:

- No duplicate `customer_id` values.
- All `email` values contain `@` with a domain part.
- All `spend` values are non-negative (>= 0).
- All `signup_date` values are parseable dates or empty.
- All `active` values are `Yes` or `No`.
- All `city` values are standardized (no `'PUNE'`, `'mumbai'`, `'Bngalore'`).
- No `NOT_AVAILABLE` in `phone` column.
- No `NaN` or `None` literal strings in `category` column.

### 5. Visualization Check

Open `3_data_cleaning_report.png`:

- Left subplot: bar chart with 5 categories (Total Rows, Duplicates, Bad Emails, Bad Dates, Neg Spend).
- Right subplot: city distribution with standardized city names.

## Regression Testing

Before committing changes, always:

1. Run the script from scratch.
2. Confirm the total issue count matches source logic: `invalid_dates + neg_spend + (before - after)`.
3. Verify no new issue types appear in the clean output.
4. Check that `cleaned_data_output.csv` is well-formed with all columns present.
