"""
004 — Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""


def vogal(letra):
    lista = ['A','E','I','O','U']
    if letra.upper() in lista:
        return "Vogal"
    elif letra.isdigit():
        return "O texto digitado não é uma letra."
    else:
        return "Consoante"


print('Descubra se a letra é VOGAL ou CONSOANTE')
letra = input('Digite uma letra: ')
print(vogal(letra))


