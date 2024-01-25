from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


def circle_move(vx0, vy0, t):
    g=10
    x = vx0 * t
    y = vy0 *t - g * t**2 / 2
    return x, y


def animate(time):
    ball.set_data(circle_move(vx0=80, vy0=14, t=time))


if __name__ == '__main__':

    fig, ax = plt.subplots()
    ball, = plt.plot([], [], 'o', color='r', label='Ball')

    edge = 400
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig,
                        animate,
                        frames=np.linspace(0, 10, 200),
                        interval=30)

    ani.save('animation_2.gif') 