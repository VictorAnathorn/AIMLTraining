import pandas as pd

# Sample DataFrame with custom index
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=['x', 'y', 'z'])

print("Original DataFrame:")
print(df)

# Resetting the index and keeping the old index as a column
df_reset = df.reset_index(drop=False)
print("\nDataFrame after resetting index (old index is kept):")
print(df_reset)

# Resetting the index and discarding the old index
df.reset_index(drop=True, inplace=True)
print("\nDataFrame after resetting index (old index is discarded):")
print(df)
