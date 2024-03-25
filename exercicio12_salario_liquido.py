#Exercício12:Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
#mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#        Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00  
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00
print('CALCULO FOLHA DE PAGAMENTO')
print()
print()
g = float(input('Quanto você ganha por hora? '))
print()
h = float(input('Quantas horas você trabalhou esse mês? '))
print()
salario =(g*h)
print(f'Salário bruto:R${salario}')
if salario <= 900:
    print('(-) IR (10%):',((salario * 0) / 1))
    IR = 0
if salario > 900 and salario <=1500:
    print('(-) IR (5%):',((salario * 5) / 100))
    IR = ((salario*5)/100)
if salario > 1500 and salario <=2500:
    print('(-) IR (10%):',((salario * 10) / 100))
    IR = ((salario*10)/100)
if salario > 2500:
    print('(-) IR (20%):',((salario * 20) / 100))
    IR = ((salario*20)/100)
INSS = ((salario * 10)/100)
print(f'(-) INSS (10%):R${INSS}')
print('FGTS (11%):',((salario * 11)/100))
print('Total de descontos:R$',(IR + INSS))
print('Salário líquido:',(salario - IR - INSS))
