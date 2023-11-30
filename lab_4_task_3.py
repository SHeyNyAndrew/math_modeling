import numpy as np

g=9.8

def energy(m, h, v):
    Ek = (m * (v ** 2)) / 2
    Ep = m * g * h
    energy = Ek * Ep
    return energy

print(energy(3, 6, 9))

e = energy(31, 64, 9)
print(e)