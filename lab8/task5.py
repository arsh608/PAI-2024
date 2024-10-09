import numpy as np
from numpy import random
arr=np.arange(1,32,2)
arr=arr.reshape(4,4)
iden= np.identity(4)
x= random.choice([2,5,9,10], size=(4,4))
print(x)
x=x*iden
print(x)
x=x+arr
print(x)
