import pandas as pd

data = {

    'Title': ['Inception', 'Dunkirk', 'Interstellar', 'The Prestige', 'Memento'],

    'Director': ['Christopher Nolan', 'Christopher Nolan', 'Christopher Nolan', 'Christopher Nolan', 'Christopher Nolan'],

    'Rating': [8.8, 7.9, 8.6, 8.5, 8.4]

}


df = pd.DataFrame(data)

print(df[df['Director'] == 'Christopher Nolan']['Rating'].mean())
