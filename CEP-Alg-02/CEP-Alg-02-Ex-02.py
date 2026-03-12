# Unidades de tempo (novamente). Neste exercício você deve fazer o processo inverso do
# exercício anterior. Desenvolva um programa Python que recebe do usuário uma quantidade de
# tempo em segundos. Então o programa deve exibir a quantidade de tempo equivalente na
# forma D:HH:MM:SS, onde D, HH, MM e SS representam dias, horas, minutos e segundos
# respectivamente. Os valores de horas, minutos e segundos devem ser formatados todos com
# dois dígitos, sendo obrigatória a inclusão do dígito 0 para valores menores que 10.

# 1 d = 86400s
# 1 h = 3600s

# print(f"{dias}:{horas:02}:{minutos:02}:{segundos:02}") formatacao pedida

total = int(input("Informe a quantidade de segundos: "))
#acumuladores
D = 0 #dias
H = 0 #horas
M = 0 #meses

if total <= 0:
    print("Esse espaço de tempo nem aconteceu!")
else:
    while total > 60:
        if total // 86400 != 0:
            D += 1
            total -= 86400
        elif total // 3600 != 0:
            H += 1
            total -= 3600
        elif total // 60 != 0:
            M += 1
            total -= 60

print(f"{D}:{H:02}:{M:02}:{total:02}")