import pandas as pd
data={
    'Names':['Ali','Sara','John','Ahmed'],
    'Marks':[65,90,85,70]
}
df=pd.DataFrame(data)
df['city']=['Lahore','Karachi','Lahore','Multan']
print(df[(df['city']=='Lahore') & (df['Marks']>70)])
