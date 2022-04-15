#  001 — Faça um Programa que peça dois números e imprima o maior deles.

print('Programa para descobrir qual número é maior')
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))

if numero1 > numero2:
    print(f'O número maior é: {numero1:.2f}')
elif numero1 < numero2:
    print(f'O número maior é: {numero2:.2f}')
else:
    print('Os números são iguais.')