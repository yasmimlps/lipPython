import numpy as np

n = int(input())

notas = np.zeros(n)
maiores = np.zeros(n)
soma = 0
cont = 0
i_maiores = 0

for i in range(n):
    notas[i] = float(input())
    soma += notas[i]

media = soma/n

for i in range(n):
    if notas[i] > media:
        maiores[i_maiores] = notas[i]
        i_maiores += 1

print(f'\nMédia = {media}')
print(f'Notas acima da média: ')
for i in range(i_maiores):
    print(maiores[i], end=' ')