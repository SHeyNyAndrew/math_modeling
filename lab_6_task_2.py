import matplotlib.pyplot as plt 
import numpy as np 

def giperbola_plotter(a=1):

    x = np.arange(-10, 10, 1)
    y = np.arange(-10, 10, 1)
    y = a/x

    plt.plot(x, y, label='mygiperbola')
    plt.xlabel('Coord - x')
    plt.ylabel('Coord - y')
    plt.title('giperbola')
    plt.legend()
    
    plt.savefig('fig_6.png')

if __name__ == '__main__':
    giperbola_plotter()