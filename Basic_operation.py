import pandas as pd
data={
    'Names':['Ali','Sara','John','Ahmed'],
    'Marks':[65,90,85,70]
}
df=pd.DataFrame(data)
print(df[df['Marks']>80])