import numpy as np
n = int(input())
saida = np.zeros(n)
entrada_1 =  np.array([float(input()) for _ in range(n)])
entrada_2 =  np.array([float(input()) for _ in range(n)])
saida = entrada_1 + entrada_2

for n in saida: 
    print(n, end=" ")