import numpy as np

def trocar_linhas(matriz, a, b):
    # Troca as linhas a e b na matriz
    matriz[a], matriz[b] = matriz[b].copy(), matriz[a].copy()

def exibir_matriz(matriz):
    # Exibe os elementos da matriz
    for linha in matriz:
        print(" ".join(map(str, linha)))

# Função principal
def main():
    # Entrada do usuário
    semente = int(input("Digite a semente do gerador de números aleatórios: "))
    num_linhas = int(input("Digite o número de linhas da matriz: "))
    num_colunas = int(input("Digite o número de colunas da matriz: "))
    a = int(input("Digite o índice da primeira linha a ser trocada: "))
    b = int(input("Digite o índice da segunda linha a ser trocada: "))
    
    # Configurar a semente do gerador de números aleatórios
    np.random.seed(semente)
    
    # Gerar matriz aleatória
    matriz_aleatoria = np.random.randint(10, 101, size=(num_linhas, num_colunas))
    
    # Exibir matriz gerada
    print("Matriz gerada:")
    exibir_matriz(matriz_aleatoria)
    
    # Trocar as linhas a e b
    trocar_linhas(matriz_aleatoria, a, b)
    
    # Exibir matriz após troca de linhas
    print("\nMatriz após troca de linhas:")
    exibir_matriz(matriz_aleatoria)

# Chamar a função principal
main()
