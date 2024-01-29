import pandas as pd

data = {'A': [1, 2, 3], 'B': [4, 5, 6]}

df = pd.DataFrame(data)
print(df)
print(df.at[1, 'B'])
print(df.loc[1, 'B'])
print(df.iloc[1, 1])
