import pandas as pd

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'City_A_Temp': [20, 22, 25, 27, 30, 32, 35, 34, 30, 28, 24, 21],
    'City_B_Temp': [10, 12, 15, 17, 20, 22, 25, 24, 20, 18, 14, 11]
}


# Write a Python program using Pandas to create a DataFrame from the given data and calculate the monthly average temperature difference between two cities.

df = pd.DataFrame(data)

df['Temp_Diff'] = abs(df['City_A_Temp'] - df['City_B_Temp'])
print("The average temperature difference between two cities is", df['Temp_Diff'].mean())
