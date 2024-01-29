import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [0, 1, 2, 3, 0, 4, 5],
    'B': [11, 12, 13, 14, 15, 16, 17],
    'C': [21, 22, 23, 24, 25, 26, 27]
})

# Calculate the mean of non-zero values in column 'A'
mean_non_zero_1 = df[df['A'] != 0]['A'].mean()
mean_non_zero_2 = df['A'][df['A'] != 0].mean()

assert mean_non_zero_1 == mean_non_zero_2

# Replace 0 values in column 'A' with the mean of non-zero values
df['A'] = df['A'].replace(0, mean_non_zero_1)

print(df)
