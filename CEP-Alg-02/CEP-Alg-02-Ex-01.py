# 1. Unidades de tempo. Crie um programa Python que leia do usuário um valor de intervalo de
# tempo expresso em número de dias, horas, minutos e segundos. O programa deve computar e
# exibir a quantidade total de segundos deste intervalo de tempo informado.

# 1 d = 86400s
# 1 h = 3600s

dias = int(input("Informe os dias: "))
hr = int(input("Informe a hora: "))
min = int(input("Informe os minutos: "))
seg = int(input("Informe os segundos: "))

total = (dias * 86400) + (hr * 3600) + (min * 6) + seg #calculo

print("A quantidade total de segundos do tempo informado é: " , total)