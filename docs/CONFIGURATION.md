# Configuration

<!-- GSD: v1.0 -->

All configuration is inline in the source files. There is no external config file.

## `3_data_cleaning_automation.py`

### Data Generation Parameters (top of script, lines 15-46)

| Parameter | Default | Description |
|---|---|---|
| `np.random.seed(42)` | `42` | Deterministic seed. Change for different random data. |
| `n = 150` | `150` | Number of records to generate. |
| `categories` | `['Electronics', 'Clothing', 'Home', 'Books', 'Sports', np.nan, np.nan]` | Product categories with 2 NaN entries (~29% missing). |
| `cities` | `['Pune', 'Mumbai', 'Delhi', 'Bangalore', 'PUNE', 'mumbai', 'New Delhi', 'Bngalore', np.nan]` | City pool with case variants, misspellings, and NaN. |
| `names` | `['Rahul Sharma', 'Priya Patel', ... , 'Ananya Gupta\n']` | Name pool with duplicates, empty strings, whitespace, None, newline. |

### Error Rate Controls (inline in data dict)

| Error Type | Control Logic | Approx Rate |
|---|---|---|
| Bad email format | `np.random.random() > 0.1` then `> 0.5` | ~10% missing `@`, ~5% empty |
| Invalid phone | `np.random.random() > 0.15` | ~15% `NOT_AVAILABLE` |
| Negative spend | `np.random.random() > 0.08` | ~8% |
| Invalid dates | `np.random.random() > 0.12` then `> 0.5` | ~12% bad format |
| Active flag chaos | Random pick from 8 values incl. empty and None | Uniform across pool |

### Cleaning Logic Parameters

| Component | What to Configure |
|---|---|
| `city_map` (line 94) | Add/remove city name mappings. 19 entries covering case variants and common misspellings for 6 cities. |
| `clean_date()` formats (line 142) | 4 format strings: `%Y-%m-%d`, `%d-%m-%Y`, `%m/%d/%Y`, `%Y/%m/%d`. Add more as needed. |
| `clean_active()` truthy list (line 160) | `['yes', 'y', 'true', '1', 'active']` — add more truthy values. |
| `clean_category()` mappings (line 124-127) | `'Home'→'Home & Kitchen'`, `'Sports'→'Sports & Fitness'`. Add more. |

### Output Paths

| Output | Hardcoded Path |
|---|---|
| Cleaned CSV | `cleaned_data_output.csv` (current dir) |
| Report PNG | `3_data_cleaning_report.png` (current dir) |

## `generate_interactive.py`

| Parameter | Default | Description |
|---|---|---|
| Chart values | Hardcoded | `values = [150, 0, 13, 18, 13]` — mirror expected output from main script |
| City distribution | Hardcoded | `cities = {'Pune': 42, 'Mumbai': 35, ...}` — edit to match actual results |
| Output file | `3_data_cleaning_interactive.html` | Current directory |

## Changing Configuration

There is no config file. To change behavior:

1. Edit the relevant parameter in the source directly.
2. Re-run the script.
3. If you changed data generation parameters, update any hardcoded values in `generate_interactive.py` and `index.html` to match.
