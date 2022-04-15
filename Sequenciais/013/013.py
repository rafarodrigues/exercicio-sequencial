"""
013 — João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
o rendimento diário de seu trabalho.

Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de
pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.

João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule
o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável
multa o valor da multa que João deverá pagar.

Imprima os dados do programa com as mensagens adequadas.
"""

from art import *

texto = text2art("Peixes\n\n\n", font='broadway', chr_ignore=True)  # Retorna o texto CALCULO com 'efeito' ASCII
print(texto)

peso = float(input('Digite o peso do peixe: '))

if peso > 50:
    excesso = peso - 50
    multa = peso + (excesso * 4)
    print('O limite no estado é de 50kg e será cobrado um valor de R$ 4,00 por kg excedente')
    print(f'O excedente foi: {excesso}')
    print(f'A multa foi: {multa}')
else:
    print(f'O limite no estado é de 50kg e seu peso foi de: {peso}kg')

