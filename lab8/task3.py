import numpy as np

arr=np.arange(2,19,2)
arr=arr.reshape(3,3)
iden= np.identity(3)
print(arr)
arr=arr*4
print(arr)
print(arr*iden)
