import numpy as np

n_linhas = int(input())
m_colunas = int(input())

matriz = np.zeros((n_linhas, m_colunas), dtype='int')
cont = 1
for i in range(n_linhas):
    for j in range(m_colunas):
        matriz[i, j] = cont
        cont +=1        

print(matriz)