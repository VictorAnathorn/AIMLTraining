import pandas as pd

# Write a Python program using Pandas to create a DataFrame from the given data and calculate the total amount spent by each customer.

data = {
    'Customer': ['Alice', 'Bob', 'Alice', 'Alice', 'Bob', 'Bob', 'Alice', 'Bob'],
    'Item': ['Pen', 'Pencil', 'Notebook', 'Eraser', 'Pen', 'Pencil', 'Notebook', 'Eraser'],
    'Price': [10, 5, 50, 20, 10, 5, 50, 20],
    'Quantity': [3, 4, 2, 5, 10, 6, 1, 2]
}

df = pd.DataFrame(data)
df['Total'] = df['Price'] * df['Quantity']
print(df.groupby('Customer').agg(Total_Spent=('Total', 'sum')))
