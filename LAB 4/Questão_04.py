# Solicita ao usuário o valor de n
n = int(input("Digite um número inteiro positivo n: "))

primeiro_termo = 0
segundo_termo = 1

contador = 0
while contador < n:
    print(primeiro_termo, end=" ")
    proximo_termo = primeiro_termo + segundo_termo
    primeiro_termo = segundo_termo
    segundo_termo = proximo_termo
    contador += 1
print() 
