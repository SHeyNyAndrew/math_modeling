from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
 
 
def circle_move(alpha):
    t = np.arange(0, 4*np.pi, 1)
    x = 12* np.cos(t) + 8* np.cos(1.5*t)
    y = 12* np.sin(t) - 8* np.sin(1.5*t)
    alpha = angle_vel * np.pi / 180 * t
    x= v0* t
    y= v0 *t -((g*t)**2)/ 2
    return x, y
 
 
def animate(i):
    ball.set_data(circle_move(R=2, angle_vel=1, t=i,g=10))
 
 
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