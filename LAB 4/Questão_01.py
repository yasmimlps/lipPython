# Solicita ao usuário que insira um número inteiro
numero = int(input("Digite um número inteiro: "))
soma = 0
calc = numero
while calc > 0:
    digito = calc % 10  
    soma += digito        
    calc = calc // 10  

print(f"A soma dos dígitos de {numero} = {soma}")

