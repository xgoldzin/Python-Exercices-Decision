print('VALORES DECRESCENTES')
print()
print()
n1 = float(input('Informe um número: '))
print()
n2 = float(input('Informe um número: '))
print()
n3 = float(input('Informe um número: '))
print()
print()
vari = [n1,n2,n3]
vari_organ = sorted(vari, reverse=True)
for numeros in vari_organ:
    print(numeros)
