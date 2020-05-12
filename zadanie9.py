import numpy as np 

x = np.arange(1,10).reshape(3,3)

for i in x.flat:
    print(i)