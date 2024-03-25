#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
#O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.
nm = float(input('Informe o primeiro número :'))
print()
nm2 = float(input('Informe o segundo número: '))
print()
op = str(input('informe qual operação deseja fazer: '))
if op == '*':
    result = nm * nm2
    print('Resultado da operação:', nm * nm2)
if op == '/':
    result = nm / nm2
    print('Resultado da operação:', nm / nm2)    
if op == '+':
    result = nm + nm2
    print('Resultado da operação:', nm + nm2)  
if op == '-':
    result = nm - nm2
    print('Resultado da operação:', nm - nm2)
if result % 2 == 0:
    print('O número é par!')
else:
    print('O número é ímpar')
if result < 0:
    print('Número negativo!')
else:
    print('Número positivo')
if result.is_integer():
    print('O número é inteiro.')
else:
    print('O número é decimal.')
    
