#Exercicio3:Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
print('CADASTRO DE SEXO')
print()
print()
nome = input('Qual o seu nome? ')
print()
sx = input(f'Qual o seu sexo {nome}? ')
print()
if sx =='F':
    print('Sexo Feminino')
elif sx == 'M':
    print('Sexo Masculino')
else:
    print('Sexo inváldo')
