import pandas as pd

data = {
    'Customer': ['Alice', 'Bob', 'Alice', 'Alice', 'Bob', 'Bob', 'Alice', 'Bob'],
    'Item': ['Pen', 'Pencil', 'Notebook', 'Eraser', 'Pen', 'Pencil', 'Notebook', 'Eraser'],
    'Price': [10, 5, 50, 20, 10, 5, 50, 20],
    'Quantity': [3, 4, 2, 5, 10, 6, 1, 2]
}

# Write a Python program using Pandas to create a DataFrame from the given data and find the total amount spent per item, as well as the total amount spent by all customers.

df = pd.DataFrame(data)
df['Spent'] = df['Price'] * df['Quantity']
print("Total spent per item:")
print(df.groupby('Item').agg(Total_Spent=('Spent', 'sum')))
print("Total spent by all customers:")
print(df['Spent'].sum())
