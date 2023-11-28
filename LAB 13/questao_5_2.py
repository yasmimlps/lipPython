import numpy as np
tamanho_a = int(input())
vetor_a = np.zeros(tamanho_a)

for i in range(tamanho_a):
    vetor_a[i] = float(input())

tamanho_b = int(input())
vetor_b = np.zeros(tamanho_b)

for i in range(tamanho_b):
    vetor_b[i] = float(input())

tamanho_c = tamanho_a + tamanho_b
vetor_c = np.zeros(tamanho_c)
print("vetor c ", vetor_c)

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

print(vetor_a)
print(vetor_b)
print(vetor_c)