import pandas as pd

data = {
    'Names': ['ali', 'SARA', 'John', 'ahmed', 'Zara'],
    'Marks': [65, 90, 85, 70, 95]
}

df = pd.DataFrame(data)
print(df[df['Names'].str.contains('a',case=False)])
#But if we want to print only Names column then we will write
print('Only Names:')
print(df[df['Names'].str.contains('a',case=False)]['Names'])