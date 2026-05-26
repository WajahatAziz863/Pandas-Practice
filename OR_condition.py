import pandas as pd

data = {
    'Names': ['Ali', 'Sara', 'John', 'Ahmed'],
    'Marks': [65, 90, 85, 70],
    'city': ['Lahore', 'Karachi', 'Lahore', 'Multan']
}

df = pd.DataFrame(data)
print(df[(df['city']=='Karachi') | (df['Marks']>80)])
