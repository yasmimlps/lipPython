import numpy as np
tamanho_a = int(input())
tamanho_b = int(input())

vetor_a = np.array([float(input()) for _ in range(tamanho_a)])
vetor_b = np.array([float(input()) for _ in range(tamanho_b)])

tamanho_c = tamanho_a + tamanho_b
vetor_c = np.zeros(tamanho_c)

i, j, k = 0, 0, 0
while k < tamanho_c:
    if i < tamanho_a:
        vetor_c[k] = vetor_a[i]
        i += 1
        k += 1

    if j < tamanho_b:
        vetor_c[k] = vetor_b[j]
        j += 1
        k += 1

print("Vetor entrelacado:")
for n in vetor_c: 
    print(n, end=" ")