import numpy as np
m=50
h=30
v=10
g=9.8

def energy(m, h, v, g):
    Ek = (m * (v ** 2)) / 2
    Ep = m * g * h
    energy = Ek * Ep
    return energy
print(energy)