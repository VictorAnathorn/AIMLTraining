import pandas as pd

# Sample data
data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 5, 8, 2, 12],
        'C': [20, 15, 18, 22, 25]}

# Create a DataFrame
df = pd.DataFrame(data)

# Sort the DataFrame based on column 'B' in ascending order
df_sorted = df.sort_values(by='B')

# Display the sorted DataFrame
print(df_sorted)
