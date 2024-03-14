import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определяем переменную величину
frames = 365
seconds_in_year = 365 * 24 * 60 * 60
seconds_in_day = 24 * 60 * 60
years = 0.5
t = np.linspace(0, years*seconds_in_year, frames)

# Определяем функцию для системы диф. уравнений
def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3) = s

    # Динамика первого тела под влиянием второго и третьего
    dxdt1 = v_x1
    dv_xdt1 = (
      	    - G * m2 * (x1 - x2) 
               / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
            - G * m3 * (x1 - x3) 
               / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
            + k * q1 * q2 / m1 * (x1 - x2) 
               / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
            + k * q1 * q3 / m1 * (x1 - x3) 
               / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
              )
    dydt1 = v_y1
    dv_ydt1 = (
      	    - G * m2 * (y1 - y2)
               / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
            - G * m2 * (y1 - y3)
               / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
            + k * q1 * q2 / m1 * (y1 - y2)
               / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
            + k * q1 * q3 / m1 * (y1 - y3)
               / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
    	      )

    # Динамика второго тела под влиянием первого и третьего
    dxdt2 = v_x2
    dv_xdt2 = (
      	    - G * m1 * (x2 - x1)
               / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
            - G * m3 * (x2 - x3)


