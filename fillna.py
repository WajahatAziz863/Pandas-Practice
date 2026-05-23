import pandas as pd

data = {
    'Names': ['Ali', 'Sara', 'John', 'Ahmed'],
    'Marks': [80, None, 75, None]
}

df = pd.DataFrame(data)
df['Marks']=df['Marks'].fillna(df['Marks'].mean())
print(df[df['Marks']>75])