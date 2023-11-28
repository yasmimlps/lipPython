import numpy as np

def func_inv(v, n):
    ult = v[n-1]

    for i in range(n-1, 0, -1):
        v[i] = v[i-1]

    v[0] = ult

    return v

s = int(input())
n = int(input())
p = int(input())
q = int(input())

np.random.seed(s)

array = np.random.randint(p, q, n)
print('Vetor gerado:')
for _ in array: 
    print(_, end=" ")

print("")
array_inv = func_inv(array, n)

print('Vetor apos deslocamento:')
for _ in array_inv: 
    print(_, end=" ")
