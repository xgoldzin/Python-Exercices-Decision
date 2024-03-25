#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
#O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal. 
print('CALCULADORA AVANÇADA')
print()
print()
nm1 = int(input('Informe o primeiro número: '))
nm2 = int(input('Informe o segundo número: '))
op = str(input('Deseja fazer uma operação de:Adição(+),Subtração(-),Multiplicação(x) ou divisão(/).'))
print()
adicao = (nm1 + nm2)
subt = (nm1 - nm2)
vezes = (nm1 * nm2)
div = (nm1 / nm2)
if op == ('+'):
    print(f'Resultado da Operação:', adicao)
    if adicao % 2 == 0:
        print('O resultado é par.')
    else:
        print('O resultado é ímpar')
    if adicao >= 0:
        print('O resultado é positivo.')
    else:
        print('O resultado é negativo.')
    if adicao // 1 == adicao:
        print('Número Inteiro')
    else:
        print('Número Decimal.')
if op == ('-'):
    print(f'Resultado da Operação:', subt)
    if subt % 2 == 0:
        print('O resultado é par.')
    else:
        print('O resultado é ímpar')
    if subt >= 0:
        print('O resultado é positivo.')
    else:
        print('O resultado é negativo.')
    if subt // 1 == subt:
        print('Número Inteiro')
    else:
        print('Número Decimal.')
    
if op == ('x'):
    print(f'Resultado da Operação:', vezes)
    if vezes % 2 == 0:
        print('O resultado é par.')
    else:
        print('O resultado é ímpar')
    if vezes >= 0:
        print('O resultado é positivo.')
    else:
        print('O resultado é negativo.')
    if vezes // 1 == vezes:
        print('Número Inteiro')
    else:
        print('Número Decimal.')
    
if op == ('/'):
    print(f'Resultado da Operação:', div)
    if div % 2 == 0:
        print('O resultado é par.')
    else:
        print('O resultado é ímpar')
    if div >= 0:
        print('O resultado é positivo.')
    else:
        print('O resultado é negativo.')
    if div // 1 == div:
        print('Número Inteiro')
    else:
        print('Número Decimal.')
    
