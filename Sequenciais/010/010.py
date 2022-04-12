# 010 - Faça um Programa que peça a temperatura em graus Celsius,
# transforme e mostre em graus Fahrenheit. C = 5 * ((F-32) / 9)


def temp_CtoF():
    temp_c = float(input('Digite a temperatura em Celsius: '))
    print(f'{temp_c: .2f}°C em Celsius é: {((temp_c * 1.8) + 32): .2f}')


def main():
    temp_CtoF()


main()

