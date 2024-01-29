import pandas as pd

data = {
    'Product': ['A', 'B', 'C', 'A', 'B', 'C'],
    'Price': [100, 200, 300, 150, 250, 350],
    'Quantity': [10, 5, 7, 12, 8, 5]
}

df = pd.DataFrame(data)

total_revenue = (df['Price'] * df['Quantity']).sum()
average_price = df['Price'].mean()
print(total_revenue, average_price)
