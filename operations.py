import pandas as pd
sale={
    'Product':['Laptop','Mobile','Tablet'],
    'Price':[50000,30000,15000]
}
tab=pd.DataFrame(sale)
#Adding Discounted price column 10%
tab['Discounted price']=tab['Price']*.9
print(tab)

