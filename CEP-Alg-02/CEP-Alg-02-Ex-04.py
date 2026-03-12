# Ordenação de 3 inteiros. Crie um programa que obtém 3 números inteiros do usuário e os
# exibe de forma ordenada do menor para o maior. Use as funções min e max para encontrar o
# menor valor e o maior valor. Dica: o valor do meio pode ser obtido pela soma dos três valores,
# subtraída do maior e do menor.

#entrada
x = int(input("Insira um número: "))
z = int(input("\nInsira mais um número: "))
y = int(input("\nInsira um número de novo: "))

print("Núemros em ordem: \n", min(x,z,y), "\n", (z+y+x) - max(z,y,x) - min(z,x,y), "\n", max(z,x,y))