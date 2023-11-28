import numpy as np

def produto_coluna(matriz, indice_coluna):
    coluna = matriz[:, indice_coluna]
    resultado = 1
    for valor in coluna:
        resultado *= valor
    return resultado
semente = int(input())
# np.random.seed(semente)

num_linhas = int(input())
num_colunas = int(input())
indice_coluna = int(input())

matriz_aleatoria = np.random.randint(1, 11, size=(num_linhas, num_colunas))

print("\nMatriz gerada:")
print(matriz_aleatoria)

resultado = produto_coluna(matriz_aleatoria, indice_coluna)
print(f"\nProdutorio do vetor coluna {indice_coluna}: {resultado}")