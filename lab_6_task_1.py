import matplotlib.pyplot as plt 

x = [1, 5, 5, 1]
y = [1, 1, 5, 5]

plt.plot(y, x, color='r', label='Graf 1', marker='>', ms=5)
plt.plot(x, y, color='r', label='Graf 2', marker='o', ms=3)

plt.xlabel('Coord: x')
plt.ylabel('Coord: y')
plt.title('Base')
plt.axis('equal')
plt.savefig('fig_5.png')