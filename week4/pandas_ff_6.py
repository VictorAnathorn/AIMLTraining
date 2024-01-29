import pandas as pd

data = {
    'Category': ['Fruit', 'Vegetable', 'Fruit', 'Vegetable', 'Fruit', 'Vegetable'],
    'Name': ['Apple', 'Carrot', 'Banana', 'Potato', 'Grape', 'Onion'],
    'Price': [2, 1, 1.5, 0.5, 3, 1],
    'Quantity': [10, 20, 15, 30, 5, 40]
}

# Given the following DataFrame and code snippet, predict the output of the code.

df = pd.DataFrame(data)
fruits = df[df['Category'] == 'Fruit']
total_fruit_value = fruits['Price'].sum() * fruits['Quantity'].sum()
print(total_fruit_value)
