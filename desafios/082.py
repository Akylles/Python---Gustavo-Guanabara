lista = []
pares = []
impares = []

while True:
    numero = int(input('Informe um número: '))
    lista.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

    sair = input('Sair? ').strip().upper()[0]
    print()

    if sair == 'S':
        break

print('A lista inteira: {}'.format(lista))
print('Os pares: {}'.format(pares))
print('Os ímpares: {}'.format(impares))
