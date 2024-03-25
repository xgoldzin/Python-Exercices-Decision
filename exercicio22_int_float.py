#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
import math
print('INTEIRO OU DECIMAL!')
print()
print()
nm = float(input('Informe um número: '))
print()
if isinstance(nm, float):
    print("É um número decimal.")
if isinstance(nm, int):
    print("É um número inteiro.")
