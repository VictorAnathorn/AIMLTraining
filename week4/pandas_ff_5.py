import pandas as pd

data = {

    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],

    'Temperature': [20, 22, 25, 27, 30, 32, 35, 34, 30, 28, 24, 21]

}

# Write a Python program using Pandas to create a DataFrame from the given data and find the month with the highest average temperature.

df = pd.DataFrame(data)
print("The month with the highest temperature is", df.sort_values(
    by='Temperature', ascending=False).head(1).values[0][0])
