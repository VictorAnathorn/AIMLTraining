import pandas as pd

# Given the following DataFrame, write a Python program using Pandas to extract all rows where the price is greater than or equal to 20,000 and sort them in descending order by price.

data = {
    'Product': ['Laptop', 'Desktop', 'Tablet', 'Phone', 'Smartwatch'],
    'Price': [25000, 12000, 8000, 22000, 5000]
}

df = pd.DataFrame(data)

# Extract all rows where the price is greater than or equal to 20,000 and sort them in descending order by price
print(df[df['Price'] >= 20000].sort_values(by='Price', ascending=False).reset_index(drop=True))
