import pandas as pd

data = {'A': [1, 2, 3], 'B': [4, 5, 6]}

df = pd.DataFrame(data)
print(df)
print(df.apply(lambda x: x**2))
