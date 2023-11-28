import numpy as np

vetor = np.array([int(input(f"Digite o {i + 1}º número: ")) for i in range(3)])

vetor2 = np.linspace(vetor[0], vetor[1], vetor[2])
print(vetor)
print(vetor2)