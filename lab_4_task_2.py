import numpy as np
def summator(array):
    s = 1
    for i in range(len(array)):
        s*=array[i]
        return s
    
test= np.arange(1, 100,1)
print(summator(test))