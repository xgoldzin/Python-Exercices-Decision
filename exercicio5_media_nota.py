#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.
print('MEDIA ALUNO')
print()
print()
nt1 = float(input('Informe a primeira nota: '))
print()
nt2 = float(input('Informe a segunda nota: '))
print()
print()
med = (nt1 + nt2) / 2
if med == 10:
    print('Aprovado com Distinção')
elif med >= 7:
    print('Aprovado')
else:
    print('Reprovado')
