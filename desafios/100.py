from random import randint


def eh_par(numero):
    return numero % 2 == 0


def soma_par(lista):
    soma = 0

    for num in lista:
        if eh_par(num):
            soma += num
    return soma


def sorteio():
    numeros = list()

    print('Sorteando os 5 valores da lista: ', end='')
    for i in range(0, 5):
        aleatorio = randint(1, 100)
        print(f'{aleatorio}', end=' ')
        numeros.append(aleatorio)

    soma = soma_par(numeros)

    print(' PRONTO!')
    print(f'Somando os valores pares de {numeros}, temos {soma}')


sorteio()
