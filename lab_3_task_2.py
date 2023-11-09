import numpy as np
g=9.8
p = 3.14
a = p / 3
b =p / 6
h = 100 
v=np.sqrt((g * h * (np.tan(b)**2)) / (2*(np.cos(a) **2)*  (1 - (np.tan(b) * (np.tan(a))))))
print(v)



from lab_3_task_1 import k, e, h
t = 200 
p = 3.14
ε = 300
n=(2 / np.sqrt(p)) * (h / ((k*t)**3/2)) *(e ** (-ε/(k*t))) * (ε**(t/2))
print(n)
