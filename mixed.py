import pandas as pd

data = {
    'Names': ['Ali', 'Sara', 'John', 'Ahmed', 'Zara'],
    'Marks': [80, None, 85, 70, None],
    'City': ['Lahore', 'Karachi', 'Lahore', 'Multan', 'Karachi']
}

df = pd.DataFrame(data)
df['Marks']=df['Marks'].fillna(df['Marks'].mean())
print(df[(df['Marks']>75)&(df['City'].isin(['Lahore','Karachi']))])