# 004 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.<br><br>
nota1 = float(input('Digite a nota do primeiro semestre: '))
nota2 = float(input('Digite a nota do segundo semestre: '))
nota3 = float(input('Digite a nota do terceiro semestre: '))
nota4 = float(input('Digite a nota do quarto semestre: '))

print(f'A média é: {(nota1+nota2+nota3+nota4)/4: .2f}')
