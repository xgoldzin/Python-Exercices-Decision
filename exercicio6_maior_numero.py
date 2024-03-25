#Faça um Programa que leia três números e mostre o maior deles.
print('QUAL O MAIOR?')
print()
print()
n1 = input('Informe um número: ')
print()
n2 = input('Informe um número: ')
print()
n3 = input('Informe um número: ')
print()
if (n1 > n2) and (n1 > n3):
    print(f'{n1} é o maior número')
if (n2 > n1) and (n2 > n3):
    print(f'{n2} é o maior número')
if (n3 > n1) and (n3 > n2):
    print(f'{n3} é o maior número')
