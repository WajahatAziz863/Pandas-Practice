import pandas as pd
data={
    'Name' : ['Ali','Hassan','Zahid','Daari'],
    'city' : ['Berlin','Oslo','London','Karachi'],
    'Score' : [120,340,430,500]
}
new=pd.DataFrame(data)
print(new)