n = int(input())

# Inicialize o fatorial como 1
fatorial = 1

# Loop de 1 até n
for i in range(1, n + 1):
    fatorial *= i
    print(f"{i}! = {fatorial}")
