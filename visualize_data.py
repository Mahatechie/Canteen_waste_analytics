import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load raw CSV (even if it has 'Unnamed' headers)
file_path = r"D:\Downloads\Documents\canteen_analytics_project\canteen_cleaned.csv"
df_raw = pd.read_csv(file_path)

# Step 2: Find and rename actual header row
# Assume the correct headers are in row index 2 (change if needed)
new_header = df_raw.iloc[2]  # 3rd row (index 2) has actual column names
df = df_raw[3:].copy()       # Data starts after that row
df.columns = new_header      # Set correct headers
df.reset_index(drop=True, inplace=True)

# Step 3: Convert relevant columns to numeric
numeric_cols = ['Cooked Qty', 'Consumed Qty', 'Leftover Qty', 'Cost (INR)']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Step 4: Add insights
df['Wastage %'] = ((df['Leftover Qty'] / df['Cooked Qty']) * 100).round(2)
df['Cost per Plate'] = (df['Cost (INR)'] / df['Consumed Qty']).round(2)

# Step 5: Plot Wastage %
plt.figure(figsize=(10, 5))
sns.barplot(x='Dish Name', y='Wastage %', data=df, palette='coolwarm')
plt.title('Wastage Percentage by Dish')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('wastage_by_dish.png')
plt.show()

# Step 6: Plot Cost per Plate
plt.figure(figsize=(10, 5))
sns.barplot(x='Dish Name', y='Cost per Plate', data=df, palette='viridis')
plt.title('Cost per Plate by Dish')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('cost_per_plate.png')
plt.show()
