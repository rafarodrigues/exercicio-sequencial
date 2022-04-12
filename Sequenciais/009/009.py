# 009 - Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9)


def temp_FtoC():
    temp_f = float(input('Digite a temperatura em Fahrenheit: '))
    print(f'{temp_f: .2f}°F em Celsius é: {5 * ((temp_f - 32) / 9): .2f}')


def main():
    temp_FtoC()


main()