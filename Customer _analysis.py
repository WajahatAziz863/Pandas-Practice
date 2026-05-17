import pandas as pd

data = {
    'OrderID': [101,102,103,104,105,106,107],
    'City': ['Lahore','Karachi','Lahore','Multan','Karachi','Lahore','Multan'],
    'Product': ['Laptop','Mobile','Tablet','Laptop','Mobile','Tablet','Laptop'],
    'Sales': [50000,30000,20000,None,35000,22000,None],
    'Quantity': [1,2,1,1,2,1,1]
}

df = pd.DataFrame(data)
#Data Cleaning
df['Sales']=df['Sales'].fillna(df['Sales'].mean())
print(df)
#Basic Business Metrics
total_values=df['Sales'].agg(['sum','max','mean'])
print(total_values)
#City Wise Analysis
sorted_values=df.groupby('City')['Sales'].sum().sort_values(ascending=False)
print(sorted_values)
#Prodct Analysis
total_sales=df.groupby('Product')['Sales'].agg(['sum','mean'])
print(total_sales)
#Smart Filtering
print(df[(df['Sales']>25000)&(df['Quantity']>=2)])
#Now we will find out which city and which product has highest total sales.
print('Top City:',sorted_values.idxmax())
print('Top Product:',total_sales['sum'].idxmax())