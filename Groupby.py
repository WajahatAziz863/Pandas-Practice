import pandas as pd

data = {
    'Names': ['Ali', 'Sara', 'John', 'Ahmed', 'Zara'],
    'Marks': [80, 90, 85, 70, 95],
    'City': ['Lahore', 'Karachi', 'Lahore', 'Multan', 'Karachi']
}

df = pd.DataFrame(data)
print(df.groupby('City')['Marks'].mean())
print(df.groupby('City')['Marks'].max())
