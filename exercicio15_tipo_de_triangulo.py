#Exercicio15:Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;
print('TIPOS DE TRIÂNGULOS')
print()
print()
ld1 = float(input('Informe a medida do primeiro lado(Sem unidade de medida):'))
ld2 = float(input('Informe a medida do segundo lado(Sem unidade de medida):'))
ld3 = float(input('Informe a medida do terceiro lado(Sem unidade de medida):'))
print()
if ld1 + ld2 < ld3 or ld2 + ld3 < ld1 or ld2 + ld3 < ld2:
    print('As medidas informadas não formam um triângulo!')
else:
    if ld1 == ld2 and ld2 == ld3:
        print('Triângulo Esquilátero!')
    elif ld1 == ld2 and ld1 != ld3:
        print('Triângulo Isósceles!')
    else:
        print('Triãngulo Escaleno!')
