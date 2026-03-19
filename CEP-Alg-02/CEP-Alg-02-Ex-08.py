# Centena, dezena, unidade (novamente). Dado um número de três algarismos N = CDU
# (onde C é o algarismo das centenas, D é o algarismo das dezenas e U o algarismo das
# unidades), considere o número M constituído pelos algarismos de N em ordem inversa, isto é,
# M=UDC. Faça um programa Python para gerar e imprimir M a partir de N (p.ex.:N=123
# ->M=321).

n = int(input("Informe o numero desejado: "))

#c = n // 100
d = (n % 100) // 10
u = d % 10

print("N: ", n // 100, "" , (n % 100) // 10, "", d % 10)
print("M: ", d % 10, "", (n % 100) // 10, "", n // 100)