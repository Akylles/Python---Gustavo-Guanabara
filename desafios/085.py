numeros = [[], []]

for i in range(0, 7):
    valor = int(input('Digite o {}º número: '.format(i + 1)))

    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

print('-=' * 30)

print('Os números pares em ordem crescente: {}'.format(sorted(numeros[0])))
print('Os números ímpares em ordem crescente: {}'.format(sorted(numeros[1])))
