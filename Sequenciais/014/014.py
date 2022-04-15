"""
014 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
    11% para o Imposto de Renda
    8% para o INSS
    5% para o sindicato
Faça um programa que nos dê:
    * salário bruto.
    * quanto pagou ao INSS.
    * quanto pagou ao sindicato.
    * o salário líquido.
Calcule os descontos e o salário líquido, conforme a tabela abaixo:
    Salário Liquido = Salário Bruto - IR (11%) - INSS (8%) - Sindicato ( 5%)
    Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
from art import *

texto = text2art("PAGAMENTO\n\n\n", font='tarty1', chr_ignore=True)  # Retorna o texto CALCULO com 'efeito' ASCII
print(texto)

salariohora = float(input('Digite o quanto você ganha por hora. R$ '))
horames = int(input('Digite quantas horas você trabalhou no mês: '))

salariobruto = salariohora * horames
print(f'\nValor bruto é: R$ {salariobruto:0.2f}')
print(f'Valor pago de IR (11%): R$ {salariobruto * 0.11:.2f}')
print(f'Valor pago de INSS (8%): R$ {salariobruto * 0.08:.2f}')
print(f'Valor pago para o sindicato (5%): R$ {salariobruto * 0.05:.2f}')
print(f'Salário líquido: R$ {salariobruto - salariobruto * 0.11 - salariobruto * 0.08 - salariobruto * 0.05:.2f}')
