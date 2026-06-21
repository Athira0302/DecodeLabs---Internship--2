import pandas as pd
import numpy as np

# =========================================================================
# STAGE 1: INPUT - Loading the Excel Spreadsheet (.xlsx)
# =========================================================================
# Updated with your exact file name
file_name = "Dataset for Data Analytics (1).xlsx"

try:
    df = pd.read_excel(file_name, engine='openpyxl')
    print("--- [STAGE 1: INPUT] ---")
    print(f"✅ Success: Loaded '{file_name}' using openpyxl engine.")
    print(f"📁 Dimensions: {df.shape[0]} transaction lines, {df.shape[1]} columns\n")
except FileNotFoundError:
    print(f"❌ Error: Could not find '{file_name}' in this folder.")
    print("Please check that the file is placed in the exact same folder open in VS Code.")
    exit()
except ImportError:
    print("❌ Error: Missing the 'openpyxl' engine dependency.")
    print("Please run this command first in a cell or terminal to fix it: pip install openpyxl")
    exit()

# =========================================================================
# STAGE 2: PROCESS - Executing Mathematical & Statistical Diagnostics
# =========================================================================
print("--- [STAGE 2: PROCESS] ---")

# 1. Missing Value Check (Data Completeness)
missing_counts = df.isnull().sum()
total_cells = df.size
total_missing = missing_counts.sum()
completeness_rate = ((total_cells - total_missing) / total_cells) * 100
print(f"🔹 Data Completeness Rate: {completeness_rate:.2f}%")
if total_missing > 0:
    print("Missing data summary per column:")
    print(missing_counts[missing_counts > 0], "\n")
else:
    print("🔬 Diagnostics: Perfect dataset integrity. No missing cells found.\n")

# 2. Date Column Format Audit
df['Cleaned_Date'] = pd.to_datetime(df['Date'], errors='coerce')
date_anomalies = df['Cleaned_Date'].isna().sum()
print(f"🔹 Temporal Structure Anomalies: {date_anomalies} invalid dates found.\n")

# 3. The Logic Skeleton: Five-Number Summary
print("🔹 Logic Skeleton (Five-Number Summary Blueprint):")
target_metrics = ['Quantity', 'UnitPrice', 'TotalPrice']
summary_table = df[target_metrics].describe().loc[['count', 'mean', '50%', 'min', '25%', '75%', 'max']]
summary_table = summary_table.rename(index={'50%': 'median (50%)'})
print(summary_table, "\n")

# 4. Distribution Geometry (Mean vs Median Check)
print("🔹 Distribution Geometry Diagnosis:")
for col in ['UnitPrice', 'TotalPrice']:
    mean_val = df[col].mean()
    median_val = df[col].median()
    print(f" [{col}] Mean (Average): {mean_val:.2f} | Median: {median_val:.2f}")
    
    if abs(mean_val - median_val) > (median_val * 0.1):
        print(f"   ⚠️ Direction: Distribution is SKEWED. Use Median to represent the center.")
    else:
        print(f"   ⚖️ Direction: Distribution is SYMMETRICAL. Mean can be safely reported.")
print("\n")

# =========================================================================
# STAGE 3: OUTPUT - Summary Deliverables
# =========================================================================
print("--- [STAGE 3: OUTPUT] ---")
print(f"🔹 Operational Revenue Peak (Max Line Item) : ${df['TotalPrice'].max():,.2f}")
print(f"🔹 Minimum Single Line Item Spend           : ${df['TotalPrice'].min():,.2f}")
print(f"🔹 Total Combined Revenue Tracked           : ${df['TotalPrice'].sum():,.2f}")

print("\n🔹 Transactional Distribution by OrderStatus:")
print(df['OrderStatus'].value_counts())