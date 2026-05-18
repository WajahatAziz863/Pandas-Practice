import pandas as pd
data={
    'Names':['Ali','Sara','john'],
    'Ages':[20,19,22],
    'Cities':['Lahore','Karachi','Islamabad']
}
var=pd.DataFrame(data)
print(var)
print('Only ages:')
print(var['Ages'])