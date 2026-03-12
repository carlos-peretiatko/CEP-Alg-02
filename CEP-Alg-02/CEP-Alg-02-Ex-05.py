# Calculando o troco. Considere o software que controla uma máquina automática de compras.
# Uma tarefa que ele precisa realizar é determinar quanto troco fornecer ao comprador quando
# este faz o pagamento em dinheiro. Escreva um programa Python que inicia lendo do usuario
# uma quantidade de centavos como um número inteiro (portanto vamos considerar números de
# 0 a 99). Então o seu programa deve calcular e exibir quantidade e o valor de cada moeda para
# compor este troco em centavos informado. O troco deve ser montado com a menor quantidade
# possível de moedas. Assuma que a máquina possui moedas de 50, 25, 10, 5 e 1 centavos.

troco = int(input("Informe o valor do seu troco (0 - 99): "))
c50 = 0 #acumulador de 50
c25 = 0 #acumulador de 25
c10 = 0 #acumulador de 10
c5 = 0 #acumulador de 5
c1 = 0 #acumulador de 1

if troco > 99 or troco < 0:
    print("\nNão está entre o intervalo permitido:\n0 - 99")
elif troco == 0:
    print("\nVocê não precisa de troco!!")
else:
    while troco != 0:
        if troco // 50 != 0: # caso o quaciente do troco atual seja divisivel, mesmo com resto executa
            troco -= 50 #atribui o valor do resto
            c50 += 1
        elif troco // 25 != 0:
            troco -=25
            c25 += 1
        elif troco // 10 != 0:
            troco -=10
            c10 += 1
        elif troco // 5 != 0:
            troco -= 5
            c5 += 1
        else: #caso nao tenha mais divisao
            troco -= 1 # desconta e adiciona uma moeda
            c1 += 1

    print("\nA quantidade de moedas recebidas será: \n" , c50, " de 50c\n", c25, " de 25c\n" , c10 ," de 10c\n", c5 , " de 5c\n", c1, " de 1c")