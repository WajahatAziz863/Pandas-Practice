import pandas as pd

data = {
    'Names': ['Ali', 'Sara', 'John', 'Ahmed'],
    'Marks': [80, None, 75, None]
}

df = pd.DataFrame(data)
print(df[df['Marks'].isnull()])
print(df[df['Marks'].notnull()])