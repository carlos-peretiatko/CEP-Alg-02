# Centena, dezena, unidade. Dado um número de três algarismos N = CDU (onde C é o
# algarismo das centenas, D é o algarismo das dezenas e U o algarismo das unidades) Faça um
# programa Python que receba do usuário o número inteiro N, e imprima separadamente a
# centena, a dezena e a unidade.

n = int(input("Informe o numero desejado: "))

c = n // 100
d = (n % 100) // 10
u = d % 10

print("D: ", c ,"\nD: ", d ,"\nU: ", u)