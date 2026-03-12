# Soma dos dígitos de um inteiro. Desenvolva um programa que obtenha do usuário um
# número inteiro de 4 dígitos e exiba a soma dos dígitos do número. Por exemplo, se o usuário
# fornecer o número 3141, então seu programa deve exibir o número 9 (3 + 1 + 4 + 1).

num = int(input("Informe um número, de preferencia de 4 digitos: "))
resto = 0

while num > 0: 
    digito = num % 10 #pega o último dígito
    resto += digito
    num = num // 10 #remove o ultimo digito

print("\nSoma:", resto)