import numpy as np

def fatores_primos(numero):
    vetor_fatores = []
    divisor = 2
    while numero > 1:
        while numero % divisor == 0:
            vetor_fatores.append(divisor)
            numero /= divisor
        divisor += 1

    return np.array(vetor_fatores)
    
numero = int(input())
vetor_resultante = fatores_primos(numero)
print(f'Fatores primos de {numero}:')
for _ in vetor_resultante: 
    print(_, end=" ")