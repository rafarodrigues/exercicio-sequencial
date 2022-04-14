# 011 - Faça um Programa que peça 2 números inteiros e um número real.
# Calcule e mostre:
#   * o produto do dobro do primeiro com metade do segundo.
#   * a soma do triplo do primeiro com o terceiro.
#   * o terceiro elevado ao cubo.

from art import *


def numeros():
    texto = text2art("CALCULO\n\n\n", font='tarty1', chr_ignore=True)  # Retorna o texto CALCULO com 'efeito' ASCII
    print(texto)

    print('Digite 2 números inteiros e 1 número real.')
    num1 = int(input('Digite um número inteiro: '))
    num2 = int(input('Digite outro número inteiro: '))
    num3 = float(input('Digite um número real: '))
    print(f'O produto do dobro do primeiro ({num1}), com metade do segundo({num2}) é: {(num1 * 2) * (num2 / 2):.2f}')
    print(f'A soma do triplo do primeiro ({num1}) com o terceiro ({num3:.0f}) é: {(num1 * 3) + num3:.2f}')
    print(f'o terceiro ({num3:.0f}) elevado ao cubo é: {num3 ** 3:.2f}')

    # return num1, num2, num3


def main():
    numeros()


main()
