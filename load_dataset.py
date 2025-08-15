import pandas as pd

# Step 1: Load the CSV while skipping top 2 rows (junk)
file_path = r"D:\Downloads\Documents\canteen_analytics_project\canteen_cleaned.csv"
df_raw = pd.read_csv(file_path, skiprows=2)

# Step 2: Drop columns that are completely empty
df_raw.dropna(axis=1, how='all', inplace=True)

# Step 3: Rename columns using the correct header row (the 1st row in this cleaned df)
df_raw.columns = df_raw.iloc[0]  # first row contains correct column names
df = df_raw[1:].copy()           # remove the header row from data

# Step 4: Reset index
df.reset_index(drop=True, inplace=True)

# Step 5: Show cleaned data
print("✅ Cleaned DataFrame Preview:\n")
print(df.head())

# Convert numeric columns
numeric_cols = ['Cooked Qty', 'Consumed Qty', 'Leftover Qty', 'Cost (INR)']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Add Wastage % column
df['Wastage %'] = (df['Leftover Qty'] / df['Cooked Qty']) * 100
df['Wastage %'] = df['Wastage %'].round(2)

# Add Cost per Plate column
df['Cost per Plate'] = df['Cost (INR)'] / df['Consumed Qty']
df['Cost per Plate'] = df['Cost per Plate'].round(2)

# Preview updated DataFrame
print("\n📊 Updated DataFrame with Insights:\n")
print(df.head())

