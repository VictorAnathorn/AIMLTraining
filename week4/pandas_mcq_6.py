import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}, index=['row1', 'row2', 'row3', 'row4'])

print(df)

# Drop a row by index
df_dropped = df.drop('row2')

print(df_dropped)
