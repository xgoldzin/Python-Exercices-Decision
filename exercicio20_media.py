#Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.
print('APROVADO OU REPROVADO?')
print()
print()
n1 = float(input('Informe a primeira nota parcial: '))
n2 = float(input('Informe a segunda nota parcial: '))
n3 = float(input('Informe a terceira nota parcial: '))
print()
media = (n1 + n2 + n3) / 3
if media >= 7 and media < 9.9:
    print('Aprovado')
    print(f'Sua média foi:{media}')
elif media < 7:
    print('Reprovado')
    print(f'Sua média foi:{media}')
else:
    print('Aprovado com Distinção')
    print(f'Sua média foi:{media}')
                      
