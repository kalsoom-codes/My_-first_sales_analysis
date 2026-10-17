import pandas as pd
import matplotlib.pyplot as plt

# --- My First Data Project - Hyderabad ---
data = {
    'Date': ['2024-01-03','2024-01-06','2024-01-09','2024-01-12','2024-01-13','2024-01-17','2024-01-20','2024-01-23','2024-01-27','2024-01-30','2024-01-31','2024-02-03','2024-02-08','2024-02-09','2024-02-12','2024-02-16','2024-02-19','2024-02-22','2024-02-25','2024-02-29','2024-03-02','2024-03-05','2024-03-09','2024-03-11','2024-03-13'],
    'Product': ['Mobile','Laptop','Headphone','Charger','Smart Watch','Mobile','Laptop','Headphone','Charger','Smart Watch','Mobile','Laptop','Headphone','Charger','Smart Watch','Mobile','Laptop','Headphone','Charger','Smart Watch','Mobile','Laptop','Headphone','Charger','Smart Watch'],
    'Region': ['Hyderabad','Karachi','Lahore','Sukkur','Islamabad','Hyderabad','Karachi','Lahore','Sukkur','Islamabad','Hyderabad','Karachi','Lahore','Sukkur','Islamabad','Hyderabad','Karachi','Lahore','Sukkur','Islamabad','Hyderabad','Karachi','Lahore','Sukkur','Islamabad'],
    'Sales': [54379,137269,5225,2331,15966,47165,135417,6449,3318,20050,79568,132497,4306,1672,14122,47620,115516,7176,1860,17982,63422,110559,3302,3208,24611],
    'Quantity': [1,3,2,1,3,3,2,1,1,3,3,3,3,3,2,3,2,1,3,2,1,1,1,1,2]
}

df = pd.DataFrame(data)

# Analysis
print("--- Region Wise Sales ---")
print(df.groupby('Region')['Sales'].sum().sort_values(ascending=False))

print("\n--- Product Wise Sales ---")
print(df.groupby('Product')['Sales'].sum().sort_values(ascending=False))

print(f"\nTotal Sales: {df['Sales'].sum()} Rs")
print(f"Average Sales: {int(df['Sales'].mean())} Rs")
print(f"Total Rows: {len(df)}")

# Save to Excel (for local use)
# df.to_excel('Sales_25_Rows.xlsx', index=False)

# Graph
df.groupby('Region')['Sales'].sum().plot(kind='bar', color='orange')
plt.title('Pakistan Region Sales - My First Project')
plt.ylabel('Sales (Rs)')
plt.show()
