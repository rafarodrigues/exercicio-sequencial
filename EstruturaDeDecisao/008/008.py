# 008 - Faça um programa que pergunte o preço de três produtos
# e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.


from art import *
texto = text2art("008\n\n\n", font='tarty1', chr_ignore=True)  # Retorna o texto com 'efeito' ASCII
print(texto)

print('Digite o preço dos 3 produtos para calcular qual o melhor.')
preco1 = float(input('Digite o preço do produto 1: '))
preco2 = float(input('Digite o preço do produto 2: '))
preco3 = float(input('Digite o preço do produto 3: '))


if (preco1 < preco2) and (preco1 < preco3):
    print('1')
elif preco2 < preco3:
    print('2')
else:
    print('3')
