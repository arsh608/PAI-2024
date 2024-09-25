import pandas as pd
#dictionaries can be directly assigned as columns and aligned
d={'name':['a','b','c','d'], 'age':[55,66,77,88]}
print(d)
df= pd.DataFrame(d)
print(df)

#nested arrays can be directly assigned as records in rows
#and column must be provided.
a=[['a', 55], ['b',66],['c',77],['d',88]]
ld= pd.DataFrame(a, columns= ['name','age'])
print(ld)
ld.to_csv('data1.csv')

#data=pd.read_csv(r'path/filename.ext')

