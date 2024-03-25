#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências,
#informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import math
print('CALCULO DAS RAÍZES DE UMA EQUAÇÃO')
print()
print()
a = int(input('Informe o valor de A:'))

if a == 0:
    print('Se A for igual a 0 a equação não é do segundo grau!')
    quit

else:
    b = int(input('Informe o valor de B:'))
    c = int(input('Informe o valor de C:'))
    delta = b ** 2 - 4* a * c
if delta < 0:
    print('A equação não possui raízes reais!')
    quit
elif delta == 0:
    raiz = -b / (2 * a)
    print(f'{raiz}')
else:
    raiz_quad = math.sqrt(delta)
    raiz_1 = (-b + raiz_quad )/ 2 * a
    raiz_2 = (-b - raiz_quad)/ 2 * a
    print(f'Raiz 1: {raiz_1}, Raiz 2: {raiz_2}')
