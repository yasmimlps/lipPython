import numpy as np

def soma(matriz, ordem):
    soma = 0
    for i in range(ordem):
        for j in range(ordem):
            if i > j:
               soma += matriz[i,j]
    return soma
        

def exibir_matriz(matriz, ordem_matriz):
    for i in range(ordem_matriz):
        for j in range(ordem_matriz):
            print(matriz[i,j], end=' ')
        print()


semente = int(input())
ordem_matriz = int(input())


np.random.seed(semente)
matriz_aleatoria = np.random.randint(1, 10, size=(ordem_matriz, ordem_matriz))

print('Matriz gerada:')
exibir_matriz(matriz_aleatoria, ordem_matriz) 
somainfeiror = soma(matriz_aleatoria, ordem_matriz)
print(f'Soma abaixo da diagonal principal: {somainfeiror}')
