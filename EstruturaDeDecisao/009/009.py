# 009 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

lista = []

numero1 = int(input('Digite o número 1: '))
numero2 = int(input('Digite o número 1: '))
numero3 = int(input('Digite o número 1: '))


lista.append(numero1)
lista.append(numero2)
lista.append(numero3)

ordem = sorted(lista, reverse= True)
print(f'Ordem decrescente:  {ordem[0]}, {ordem[1]}, {ordem[2]}.')
