import numpy as np

semente = int(input("Digite a semente do gerador de números aleatórios: "))
tamanho = int(input("Digite o tamanho do vetor: "))
p = int(input("Digite o valor mínimo (p): "))
q = int(input("Digite o valor máximo (q): "))

def deslocamento_direita_vetor_aleatorio(semente, tamanho, p, q):
    np.random.seed(semente)
    vetor_aleatorio = np.random.randint(p, q+1, tamanho)
  
    print("Vetor gerado:")
    for _ in vetor_aleatorio: 
        print(_, end=" ")

    ultimo_elemento = vetor_aleatorio[-1]
    for i in range(tamanho-1, 0, -1):
        vetor_aleatorio[i] = vetor_aleatorio[i-1]
    vetor_aleatorio[0] = ultimo_elemento

    print("\nVetor apos deslocamento:")
    for _ in vetor_aleatorio: 
        print(_, end=" ")   
 

deslocamento_direita_vetor_aleatorio(semente, tamanho, p, q)
