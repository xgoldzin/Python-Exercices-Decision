#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
#As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
#O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
import math
saque = float(input('Informe o valor a ser sacado: '))
if saque < 10 or saque > 600:
    print('Insira um valor entre 10 e 600!')
else:
    cem = saque / 100
    cem_reais = math.floor(cem)
    dezreais = (saque // 10) % 10
    if dezreais == 5:
        cinquenta = (saque % 100) / 50
        cinquentas = math.floor(cinquenta)
    unidades = saque % 10
    print(f'Serão precisos {cem_reais} notas de R$100,00,{cinquentas} notas de R$50,00, {dezreais} notas de R$10,00 reais e {unidades} notas de R$1,00')
