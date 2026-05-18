import pandas as pd
info={
    'Students':['Ali','Sara','John','Ahmed'],
    'Marks':[65,76,80,77]
}
df=pd.DataFrame(info)
print(df['Marks'].mean())