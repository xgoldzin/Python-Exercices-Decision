#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
import math
print('MOSTRANDO UNIDADES DE UM NÚMERO')
print()
print()
nm = int(input('Informe um número inteiro até 1000.'))
if nm > 1000 or nm < 1:
    print('Número Inválido!')
else:
    centenas = nm / 100
    centena = math.floor(centenas)
    dezenas = (nm // 10) % 10
    unidades = nm % 10

    print(f'{nm} = {centena} centenas, {dezenas} dezenas e {unidades} unidades.')
