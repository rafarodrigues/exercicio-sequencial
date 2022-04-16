#  007 - Faça um Programa que leia três números e mostre o maior e o menor deles.

lista = []
print('Digite 3 números para descobrir qual é o menor. ')
numero1 = input('Digite o número 1: ')
numero2 = input('Digite o número 2: ')
numero3 = input('Digite o número 3: ')

lista.append(numero1)
lista.append(numero2)
lista.append(numero3)

print(f'O menor número é: {min(lista)}')
