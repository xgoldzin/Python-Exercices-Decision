#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
print('QUAL COMPRAR?')
print()
print()
p1 = float(input('Qual o preço do 1ºproduto?'))
print()
p2 = float(input('Qual o preço do 2ºproduto?'))
print()
p3 = float(input('Qual o preço do 3ºproduto?'))
print()
if (p1 < p2) and (p1 < p3):
    print('Compre o primeiro produto!')
if (p2 < p1) and (p2 < p3):
    print('Compre o segundo produto!')
if (p3 < p1) and (p3 < p2):
    print('Compre o terceiro produto!')
