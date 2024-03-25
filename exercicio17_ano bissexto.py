#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
print('O ANO É BISSEXTO?')
print()
print()
ano = int(input('Informe o ano que deseja saber:'))
print()
if ano % 4 == 0:
    print(f'{ano} é bissexto!')
else:
    print(f'{ano} não é bissexto!')
