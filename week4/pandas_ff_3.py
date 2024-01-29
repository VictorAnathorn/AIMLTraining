import pandas as pd

data = {
    'Store': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Item': ['Apple', 'Banana', 'Orange', 'Grape', 'Apple', 'Banana', 'Orange', 'Grape'],
    'Price': [50, 20, 30, 60, 55, 22, 33, 65],
    'Quantity': [10, 12, 15, 16, 20, 25, 30, 35]
}

# Write a Python program using Pandas to create a DataFrame from the given data and find the total revenue and average price of items sold in each store.

df = pd.DataFrame(data)
df['Revenue'] = df['Price'] * df['Quantity']
print(df)

# Group by store and calculate total revenue and average price
store_summary = df.groupby('Store').agg(
    Total_Revenue=('Revenue', 'sum'),
    Average_Price=('Price', 'mean'))

print(store_summary)
