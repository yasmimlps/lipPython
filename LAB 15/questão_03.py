import numpy as np
matriz = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20]])

a = int(input())
b = int(input())
c = int(input())
d = int(input())

submatriz = matriz[b-a:b, d-c:d]
print(submatriz)