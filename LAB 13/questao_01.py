import numpy as np

vetor = np.array([0, 0, 0, 0])
for i in range(4):
    vetor[i] = int(input())


print(type(vetor))
print(vetor.size)
print(vetor.ndim)
print(vetor.shape)
print(vetor)