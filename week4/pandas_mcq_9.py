import pandas as pd

# Example 1

# Sample DataFrame
df = pd.DataFrame({
    'Product': ['Apple', 'Banana', 'Apple', 'Banana', 'Cherry', 'Cherry'],
    'Sales': [100, 200, 150, 180, 90, 120]
})

# Group by the 'Product' column and sum the 'Sales'
grouped = df.groupby('Product').sum()

print(grouped)

# Example 2

# Sample DataFrame
df = pd.DataFrame({
    'Product': ['Apple', 'Banana', 'Apple', 'Banana', 'Cherry', 'Cherry'],
    'Region': ['North', 'West', 'East', 'East', 'North', 'West'],
    'Sales': [100, 200, 150, 180, 90, 120]
})

# Group by both 'Product' and 'Region' columns
grouped = df.groupby(['Product', 'Region']).sum()

print(grouped)
