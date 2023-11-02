import numpy as np
from lab_3_task_1 import gravitation as g

alpha = np.pi / 180 * 45
v0 = 10

t = np.arange(0, 5, 0.1)
x0 = 0
y0 = 0
v0x = v0 * np.cos(alpha)
v0y = v0 * np.sin(alpha)

x =x0 + v0x * t
y = y0 + v0y * t - (((g * t)** 2)/2)
coord = np.zeros((len(t), 3))
for i in range(len(t)):
    coord[i, 0] = t[i]
    coord[i, 1] = x[i]
    coord[i, 2] = y[i]

print(coord)