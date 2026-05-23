import pandas as pd

data = {
    'Names': ['Ali', 'Sara', 'John', 'Ahmed', 'Zara'],
    'Marks': [65, 90, 85, 70, 95],
    'City': ['Lahore', 'Karachi', 'Lahore', 'Multan', 'Karachi']
}

df = pd.DataFrame(data)
print(df[df['City'].isin(['Lahore','Karachi'])])
