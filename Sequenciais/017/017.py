"""
017 - Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
from datetime import *

tamanho = float(input('Digite o tamanho do arquivo em MB: '))
velocidade = int(input('Digite a velocidade do link de internet em MBps: '))

print(f'O tempo estimado é de {(tamanho / (velocidade/8)) / 60:.2f} minutos')