import pandas as pd
info={
    'Numbers':[10,23,45,23,78]
}
df=pd.DataFrame(info)
print(df.mode())