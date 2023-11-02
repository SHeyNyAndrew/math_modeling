import numpy as np
g=9.8
p = 3.14
a = p / 3
b =p / 6
h = 100 
v=np.sqrt((g * h * (np.tan(b)**2)) / (2*(np.cos(a) **2)*  (1 - (np.tan(b) * (np.tan(a))))))
print(v)