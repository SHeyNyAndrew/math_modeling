import numpy as np

N = 6
M = 5

A = np.zeros((N, M))

A[0, 0] = 55
A[0, 1] = 61
A[0, 2] = 4
A[0, 3]= 3
A[0, 4] = 5
A[1, 0] = 7
A[1, 1] = 8
A[1, 2] = 9
A[1, 3] = 11
A[1, 4] = 10
A[2, 0] = 13
A[2, 1] = 14
A[2, 2] = 15
A[2, 3] = 16
A[2, 4] = 8
A[3, 0] = 7
A[3, 1] = 6
A[3, 2] = 4
A[3, 3] = 7
A[3, 4] = 10
A[4, 0] = 11
A[4, 1] = 7
A[4, 2] = 8
A[4, 3] = 1
A[4, 4] = 2
A[5, 0] = 10
A[5, 1] = 5
A[5, 2] = 3
A[5, 3] = 4
A[5, 4] = 8

print(A[0:2:1, 0:2:1])
print(A[2:4:1, 1:3:1])
print(A[0:2:3 ])