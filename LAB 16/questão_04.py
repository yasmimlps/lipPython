import numpy as np

def pares_acima_diagonal_principal(matriz, ordem):
    contador_pares = 0
    for i in range(ordem):
        for j in range(ordem):
            if i < j:
                if matriz[i,j]%2 == 0:
                    contador_pares +=1
    return contador_pares
        

def exibir_matriz(matriz, ordem_matriz):
    for i in range(ordem_matriz):
        for j in range(ordem_matriz):
            print(matriz[i,j], end=' ')
        print()


semente = int(input())
ordem_matriz = int(input())


np.random.seed(semente)
matriz_aleatoria = np.random.randint(10, 100, size=(ordem_matriz, ordem_matriz))

print('Matriz gerada:')
exibir_matriz(matriz_aleatoria, ordem_matriz) 
pares = pares_acima_diagonal_principal(matriz_aleatoria, ordem_matriz)
print(f'{pares} elementos pares acima da diagonal principal')
