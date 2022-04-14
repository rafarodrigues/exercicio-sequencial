# 012 - Faça um programa tendo como dados de entrada a
# altura de uma pessoa, construa um algoritmo que
# calcule seu peso ideal utilizando as seguintes fórmulas:
#   * Para homens: (72.7 * h) - 58
#   * Para mulheres: (62.1 * h) - 44.7


def pesoideal():
    print('\nPROGRAMA PARA CALCULAR PESO IDEAL\n\n')

    altura = float(input('Digite sua altura: '))
    genero = int(input('Digite o gênero que você se identifica: \n1 - Homem\n2 - Mulher \nGênero: '))

    while (genero != 1) and (genero != 2):
        print('Gênero inválido.')
        genero = int(input('Digite o gênero que você se identifica: \n1 - Homem\n2 - Mulher \nGênero: '))

    if genero == 2:
        print(f'Peso ideal para mulheres: {(62.1 * altura) - 44.7:.2f}kg')
    else:
        print(f'Peso ideal para homens: {(72.7 * altura) - 58:.2f}kg')


def main():
    pesoideal()


main()
