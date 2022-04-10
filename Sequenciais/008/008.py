# 008 - Faça um Programa que pergunte quanto você ganha
# por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

salario = float(input('Digite o valor em R$ por hora: '))
horas_mes = int(input('Digite quantas horas você trabalha por mês: '))

print(f'O salário é mensal: {(salario * horas_mes): .2f}')