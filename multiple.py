import pandas as pd

data = {
    'Names': ['Ali', 'Ali', 'Sara', 'Sara', 'John'],
    'City': ['Lahore', 'Lahore', 'Karachi', 'Karachi', 'Lahore'],
    'Subject': ['Math', 'English', 'Math', 'English', 'Math'],
    'Marks': [80, 70, 90, 85, 75]
}

df = pd.DataFrame(data)
print(df.groupby(['Names','Subject'])['Marks'].agg(['mean','max']))