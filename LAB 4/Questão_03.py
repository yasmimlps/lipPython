# Solicita ao usuário o valor de N
n = int(input("Digite o valor de N: "))

# Inicializa o valor de e como 1.0
e = 1

# Inicializa o fatorial como 1
fatorial = 1

# Calcula e com base no valor de N
for i in range(1, n + 1):
    fatorial *= i  
    e += 1 / fatorial

# Imprime o valor estimado de e
print(f"A estimativa de e com N={n} é aproximadamente {e}")
print(e)
