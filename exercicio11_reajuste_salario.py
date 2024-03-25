#Exercicio11:As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
##salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.
print('CALCULO DE SALÁRIO AJUSTADO')
print()
print()
slr = float(input('Informe o seu salário bruto atual(use ponto final ao invés de vírgula: '))
print()
print(f'Salário antes do reajuste:R${slr}')

if slr <= 280.00:
    print('20% de aumento')
elif slr > 280.00 and slr <= 700.00:
    print('15% de aumento')
elif slr > 700.00 and slr <=1500.00:
    print('10% de aumento')
else:
    print('5% de aumento')

if slr <= 280.00:
    print('Aumento de:R$',(slr *20) / 100)
elif slr > 280.00 and slr <= 700.00:
    print('Aumento de:R$',(slr *15) / 100)
elif slr > 700.00 and slr <=1500.00:
    print('Aumento de:R$',(slr * 10) /100)
else:
    print('Aumento de:R$',(slr * 5) / 100)


if slr <= 280.00:
    print('Novo Salário:R$',(slr +(slr *20) / 100))
elif slr > 280.00 and slr <= 700.00:
    print('Novo salário:R$',(slr+(slr *15) / 100))
elif slr > 700.00 and slr <=1500.00:
    print('Novo Salário:R$',(slr +(slr * 10) /100))
else:
    print('Novo salário:R$',(slr+(slr * 5) / 100))
