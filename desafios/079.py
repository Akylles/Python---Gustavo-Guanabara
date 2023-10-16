lista = []

while True:
    valor = int(input('Digite um valor: '))

    if valor not in lista:
        lista.append(valor)
    else:
        print('\033[1;31;40mO valor {} já foi adicionado e não pode ser repetido.\033[m'.format(valor))

    continuar = str(input('Deseja continuar? ')).strip().upper()[0]
    print()
    if continuar == 'N':
        break

print("A lista em ordem crescente: {}".format(sorted(lista)))
