"""
003 — Faça um Programa que verifique se uma letra digitada é "F" ou "M".

Conforme a letra escrever:
    * F — Feminino
    * M — Masculino
    * Sexo Inválido.
"""
print('Programa para descobrir se é F ou M')

genero = str(input("Digite 'F' para feminino e 'M' para masculino: "))
if genero.upper() == 'F':
    print('F - Feminino')
elif genero.upper() == 'M':
    print('M - Masculino')
else:
    print('Gênero indefinido')
