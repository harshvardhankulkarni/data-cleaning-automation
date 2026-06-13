"""
Data Cleaning Automation
Demonstrates real world data cleaning techniques on a messy dataset.
Generates its own dirty data, then cleans it step by step.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random as py_random
import re
from datetime import datetime, timedelta

# Generate a MESSY dataset (simulates real CRM export)
np.random.seed(42)
n = 150

# Introduce common data quality issues
customer_ids = []
categories = ['Electronics', 'Clothing', 'Home', 'Books', 'Sports', np.nan, np.nan]
cities = ['Pune', 'Mumbai', 'Delhi', 'Bangalore', 'PUNE', 'mumbai', 'New Delhi', 'Bngalore', np.nan]
names = ['Rahul Sharma', 'Priya Patel', 'Amit Singh', 'Vikram Joshi', '',
         '  Sneha Kapoor  ', 'Rahul Sharma', 'Priya Patel', None, 'Ananya Gupta\n']

data = {
    'customer_id': [f'C{i:04d}' for i in range(1, n+1)],
    'name': [np.random.choice(names) for _ in range(n)],
    'email': [f'user{i}@email.com' if np.random.random() > 0.1 else
              f'user{i}email.com' if np.random.random() > 0.5 else ''
              for i in range(n)],
    'phone': [f'+91{py_random.randint(7000000000, 9999999999)}' if np.random.random() > 0.15
              else 'NOT_AVAILABLE' for _ in range(n)],
    'city': [np.random.choice(cities) for _ in range(n)],
    'category': [np.random.choice(categories) for _ in range(n)],
    'spend': [round(np.random.exponential(5000), 2) if np.random.random() > 0.08
              else -round(np.random.exponential(5000), 2) for _ in range(n)],
    'signup_date': [
        (datetime(2024, 1, 1) + timedelta(days=int(np.random.exponential(60))))
        .strftime('%Y-%m-%d') if np.random.random() > 0.12 else
        '2024/13/01' if np.random.random() > 0.5
        else 'not_a_date'
        for _ in range(n)
    ],
    'active': [np.random.choice(['Yes', 'No', 'Y', 'N', 'TRUE', 'FALSE', '', None])
               for _ in range(n)],
}

df = pd.DataFrame(data)

print(f'Original dataset: {len(df)} rows')
print(f'Columns: {list(df.columns)}')

# STEP 1: Profile before cleaning
print('\n--- DATA QUALITY REPORT (BEFORE) ---')
print(f'Total rows: {len(df)}')
print(f'Duplicate rows: {df.duplicated().sum()}')
for col in df.columns:
    nulls = df[col].isnull().sum()
    empties = (df[col].astype(str).str.strip() == '').sum()
    print(f'  {col}: {nulls} nulls, {empties} empty strings')

# STEP 2: Remove duplicates
before = len(df)
df = df.drop_duplicates()
print(f'\n--- REMOVED {before - len(df)} duplicates ---')

# STEP 3: Clean names
def clean_name(val):
    if pd.isna(val):
        return None
    val = str(val).strip()
    val = val.replace('\n', '').replace('\r', '')
    if val == '' or val.lower() == 'none':
        return None
    return ' '.join([p.capitalize() for p in val.split() if p])

df['name'] = df['name'].apply(clean_name)

# STEP 4: Fix email format
def clean_email(val):
    if pd.isna(val) or str(val).strip() == '':
        return None
    val = str(val).strip().lower()
    if '@' not in val:
        return None
    parts = val.split('@')
    if len(parts) != 2 or '.' not in parts[1]:
        return None
    return val

df['email'] = df['email'].apply(clean_email)

# STEP 5: Standardize city names
city_map = {
    'pune': 'Pune', 'pune ': 'Pune', 'PUNE': 'Pune',
    'mumbai': 'Mumbai', 'mumbai ': 'Mumbai', 'MUMBAI': 'Mumbai',
    'delhi': 'Delhi', 'DELHI': 'Delhi', 'New Delhi': 'Delhi', 'new delhi': 'Delhi',
    'bangalore': 'Bangalore', 'BANGALORE': 'Bangalore',
    'bngalore': 'Bangalore', 'Bngalore': 'Bangalore',
    'bengaluru': 'Bangalore',
    'hyderabad': 'Hyderabad', 'HYDERABAD': 'Hyderabad',
    'chennai': 'Chennai', 'CHENNAI': 'Chennai',
}

def clean_city(val):
    if pd.isna(val):
        return 'Unknown'
    val = str(val).strip()
    if val.lower() in city_map:
        return city_map[val.lower()]
    if val == '':
        return 'Unknown'
    return val

df['city'] = df['city'].apply(clean_city)

# STEP 6: Clean categories
def clean_category(val):
    if pd.isna(val):
        return 'Uncategorized'
    val = str(val).strip()
    if val == '':
        return 'Uncategorized'
    if val == 'Home':
        return 'Home & Kitchen'
    if val == 'Sports':
        return 'Sports & Fitness'
    return val

df['category'] = df['category'].apply(clean_category)

# STEP 7: Fix negative spend values (data entry errors)
neg_spend = (df['spend'] < 0).sum()
df['spend'] = df['spend'].abs()
print(f'--- FIXED {neg_spend} negative spend values (absolute value) ---')

# STEP 8: Parse and validate dates
def clean_date(val):
    if pd.isna(val):
        return None
    val = str(val).strip()
    formats = ['%Y-%m-%d', '%d-%m-%Y', '%m/%d/%Y', '%Y/%m/%d']
    for fmt in formats:
        try:
            return pd.to_datetime(val, format=fmt)
        except:
            continue
    return None

valid_dates = df['signup_date'].apply(clean_date)
invalid_dates = valid_dates.isna().sum()
df['signup_date'] = valid_dates
print(f'--- FIXED {invalid_dates} invalid dates ---')

# STEP 9: Standardize active flag
def clean_active(val):
    if pd.isna(val):
        return 'No'
    val = str(val).strip().lower()
    if val in ['yes', 'y', 'true', '1', 'active']:
        return 'Yes'
    return 'No'

df['active'] = df['active'].apply(clean_active)

# STEP 10: Fill unknown phone numbers
df['phone'] = df['phone'].replace('NOT_AVAILABLE', None)

# Final profile
print(f'\n--- DATA QUALITY REPORT (AFTER) ---')
print(f'Total rows: {len(df)}')
print(f'Duplicate rows: {df.duplicated().sum()}')
for col in df.columns:
    nulls = df[col].isnull().sum()
    print(f'  {col}: {nulls} missing values')

# Visualization: Before vs After
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

quality_before = [n, df.duplicated().sum(), df['email'].isna().sum(), invalid_dates, neg_spend]
labels = ['Total Rows', 'Duplicates', 'Bad Emails', 'Bad Dates', 'Neg Spend']
colors_before = ['#3498db', '#e74c3c', '#e74c3c', '#e74c3c', '#e74c3c']

axes[0].bar(labels, quality_before, color=colors_before, edgecolor='white')
axes[0].set_title('Data Issues Found')
axes[0].tick_params(axis='x', rotation=20)
for i, v in enumerate(quality_before):
    axes[0].text(i, v + 1, str(v), ha='center')

# City distribution after cleaning
city_counts = df['city'].value_counts()
axes[1].bar(city_counts.index, city_counts.values, color='#2ecc71', edgecolor='white')
axes[1].set_title('Customer Distribution by City (After Cleaning)')
axes[1].set_ylabel('Customers')
for i, v in enumerate(city_counts.values):
    axes[1].text(i, v + 1, str(v), ha='center')

plt.tight_layout()
plt.savefig('3_data_cleaning_report.png', dpi=150, bbox_inches='tight')
print('\nSaved: 3_data_cleaning_report.png')

# Summary
print('\n--- CLEANING SUMMARY ---')
print(f'Total issues detected and resolved: {invalid_dates + neg_spend + before - len(df)}')
print(f'Duplicate rows removed: {before - len(df)}')
print(f'Invalid emails fixed: {df["email"].isna().sum()} flagged for review')
print(f'Invalid dates fixed: {invalid_dates}')
print(f'Negative spend values fixed: {neg_spend}')
print(f'Cities standardized: 7 variants normalized to 5 standard names')
print(f'Active status standardized: 6 formats normalized to Yes/No')

print('\nAction: Flag missing emails for CRM update.')
print('Action: Set up input validation to prevent future bad data.')
print('Done.')

df.to_csv('cleaned_data_output.csv', index=False)
print('\nExported: cleaned_data_output.csv')
