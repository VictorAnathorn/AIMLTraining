import pandas as pd

data1 = {'common_column': [1, 2, 3],
         'data1_column': ['A', 'B', 'C']}
df1 = pd.DataFrame(data1)

data2 = {'common_column': [2, 3, 4],
         'data2_column': [10, 20, 30]}
df2 = pd.DataFrame(data2)

merged_df_1 = df1.merge(df2, on='common_column')
merged_df_2 = pd.merge(df1, df2, on='common_column')

assert merged_df_1.equals(merged_df_2)

print(merged_df_1)
print(merged_df_2)
