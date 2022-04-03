import math
# 006 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.<br><br>
# Fórmula da área do círculo: A = π . r2


raio = float(input('Digite o valor do raio: '))
print(f'A área do círculo é: {math.pi * raio**2: .2f}')
