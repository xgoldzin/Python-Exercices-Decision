#Exercício10:Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.#
print('CADASTRO DE TURNO DE ESTUDO')
print()
print()
turn = input('Em que turno você estuda?(M - Matutino, V - Vespertino ou N - Noturno) ')
print()
t1 = 'M'
t2 = 'V'
t3 = 'N'
if turn == t1:
    print('Bom dia')
elif turn == t2:
    print('Boa tarde!')
elif turn == t3:
    print('Boa noite')
else:
    print('Valor Inválido!')
