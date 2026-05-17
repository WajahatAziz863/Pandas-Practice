import pandas as pd

data = {
    'OrderID': [201,202,203,204,205,206,207],
    'City': ['Lahore','Karachi','Lahore','Multan','Karachi','Lahore','Multan'],
    'Product': ['Laptop','Mobile','Tablet','Laptop','Mobile','Tablet','Laptop'],
    'Sales': [50000,30000,20000,25000,35000,22000,27000],
    'Cost': [40000,25000,18000,26000,20000,20000,30000],
    'Quantity': [1,2,1,1,2,1,1]
}

df = pd.DataFrame(data)
#Creating new column
df['Profit']=df['Sales']-df['Cost']
print(df)
#Total,Average and maximum profit
total_values=df['Profit'].agg(['sum','mean','max']).round(2)
print(total_values)
#Total profit per city
city_wise=df.groupby('City')['Profit'].sum().sort_values(ascending=False)
print(city_wise)
#Total profit per product
product_wise=df.groupby('Product')['Profit'].sum().sort_values(ascending=False)
print(product_wise)
#Orders where profit<0(LOSS) OR profit<5000(LESS PROFIT)
print(df[(df['Profit']<5000)])
#Main Findings from Data
print('Most profitable  City:',city_wise.idxmax())
print('Most profitable Product:',product_wise.idxmax())
print('Where is company losing:')
print(df.loc[df['Profit'].idxmin()])

