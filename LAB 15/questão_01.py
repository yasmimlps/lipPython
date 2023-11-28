import numpy as np

ordem_matriz = int(input())

matriz = np.identity(ordem_matriz)

print(matriz.ndim)
print(matriz.shape)
print(matriz)