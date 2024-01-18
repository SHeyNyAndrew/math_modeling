from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
 
 
def circle_move(R, angle_vel, time, x0, y0, v0x, v0y, x, y, t, v0, g):
    alpha = angle_vel * np.pi / 180 * time
    x0 = 0
    y0 = 0
    v0x = v0 * np.cos(alpha)
    v0y = v0 * np.sin(alpha)
    x =x0 + v0x * t
    y = y0 + v0y * t - (((g * t)** 2)/2)
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
    return x, y
 
 
def animate(i):
    ball.set_data(circle_move(R=2, angle_vel=1, time=i))
 
 
if __name__ == '__main__':
 
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], 'o', color='r', label='Ball')
 
    edge = 3
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)
 
    ani = FuncAnimation(fig,
                        animate,
                        frames=180,
                        interval=30)
 
    ani.save('animation_2.gif') 