import numpy as np 

x = np.arange(0,9).reshape(3,3)
y = np.arange(0,16).reshape(4,4)

print(x)
print("")
print(y)
print("")

print(x.min(axis=1))
print(y.min(axis=1))
print(x.min(axis=0))
print(y.min(axis=0))