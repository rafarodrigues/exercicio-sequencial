#  002 Faça um Programa que peça um valor e mostre
#  na tela se o valor é positivo ou negativo.

numero = float(input('Digite um número: '))

if numero < 0:
    print('O número é negativo')
elif numero > 0:
    print('O número é positivo')
else:
    print('O número é zero')