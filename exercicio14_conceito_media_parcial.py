#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#  Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
print('MÉDIA DE DUAS NOTAS PARCIAIS')
print()
print()
n1= float(input('Informe a primeira nota parcial: '))
print()
n2 = float(input('Informe a segunda nota parcial: '))
print()
print(f'Primeira Nota:{n1} Segunda Nota:{n2}')
media = ((n1 + n2)/2)
print(f'Segua a média:{media}')
if media >= 9 and media <= 10:
    print('Conceito A')
