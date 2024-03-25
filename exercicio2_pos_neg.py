#Exercicio2Faça um Programa que peça um valor e mostre na
#tela se o valor é positivo ounegativo.
print('O NÚMERO É POSITIVO OU NEGATIVO?')
print()
print()
nome = input('Qual o seu nome? ')
print()
num1 = float(input(f'Informe um valor e descubra se ele é positivo ou negativo {nome}: '))
print()
print()
if num1 > 0:
    print(f'{num1} é positivo!')
if num1 < 0:
    print(f'{num1} é negativo!')
