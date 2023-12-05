import numpy as np


def produto_vetor_coluna(matriz, num_linhas, num_colunas, indice_vetor):
    produto = 1
    for i in range(num_linhas):
        produto *= matriz[i, indice_vetor]
    return produto

def exibir_matriz(matriz, num_linhas, num_colunas):
    for i in range(num_linhas):
        for j in range(num_colunas):
            print(matriz[i,j], end=' ')
        print()

semente = int(input())
num_linhas = int(input())
num_colunas = int(input())
indice_vetor = int(input())

np.random.seed(semente)
matriz_aleatoria = np.random.randint(1, 10, size=(num_linhas, num_colunas))

print('Matriz gerada:')
exibir_matriz(matriz_aleatoria, num_linhas, num_colunas) 
soma_vetor_coluna = produto_vetor_coluna(matriz_aleatoria, num_linhas, num_colunas, indice_vetor)
print(f'Produtorio do vetor coluna {indice_vetor}:', soma_vetor_coluna)
