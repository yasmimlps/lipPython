import numpy as np

n = int(input())
vetor = np.array([float(input()) for _ in range(n)])

vetorpar = vetor[vetor % 2. == 0]
vetorimpar = vetor[vetor % 2. != 0]

print("Números pares:")
for n in vetorpar: 
    print(n, end=" ")

print()

print("Números impares:")
for n in vetorimpar: 
    print(n, end=" ")