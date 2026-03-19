# Data invertida. Admitindo que uma data é lida pelo algoritmo em uma variável inteira, e não
# em uma variável do tipo data, crie um programa Python que leia uma data no formato
# DDMMAA e imprima essa data no formato AAMMDD, onde:
# • a letra D corresponde a dois algarismos representando o dia;
# • a letra M corresponde a dois algarismos representando o mês;
# • a letra A corresponde aos dois últimos algarismos representando o ano.
# Por exemplo: a data 110618 (11 de junho de 2018), deve ser impressa como 180611

data = int(input("Informe a data desejada: "))

# DD / MM / AA

# Bloco Dia - //10000

# Bloco Mes -- //100

# Bloco Ano - //10*10

#Divisão em blocos de 2 x 3

D = data // 10000
M = (data % 10000) // 100
A = data % 100

print(f"{A:02d} {M:02d} {D:02d}")