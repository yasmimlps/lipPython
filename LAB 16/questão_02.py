import numpy as np

def trocar_linhas(matriz, num_linhas, num_colunas, a, b):
    for i in range(num_colunas):
        aux = matriz[b,i]
        matriz[b,i] = matriz[a,i]
        matriz[a,i] = aux

def exibir_matriz(matriz, num_linhas, num_colunas):
    for i in range(num_linhas):
        for j in range(num_colunas):
            print(matriz[i,j], end=' ')
        print()

    
semente = int(input())
num_linhas = int(input())
num_colunas = int(input())
a = int(input())
b = int(input())

np.random.seed(semente)
matriz_aleatoria = np.random.randint(10, 100, size=(num_linhas, num_colunas))

print("Matriz gerada:")
exibir_matriz(matriz_aleatoria, num_linhas, num_colunas)  
trocar_linhas(matriz_aleatoria, num_linhas, num_colunas, a, b)
print("Matriz apos troca")
exibir_matriz(matriz_aleatoria, num_linhas, num_colunas)

