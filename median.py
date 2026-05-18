import pandas as pd
info={
    'Numbers':[100,123,234,56,456]
}
df=pd.DataFrame(info)
print(df.median())
#output is 123 because median is the middle value of sorted list,so pandas first sorted it in
#ascending order as [56,100,123,234,456],here middle value is 123