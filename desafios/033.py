numeros = []

for i in range(0, 3):
    num = int(input('Informe o {} número: '.format(i+1)))
    numeros.insert(i, num)

maior = numeros[0]
menor = numeros[0]

for i in range(1, 3):
    num = numeros[i]
    if num > maior:
        maior = num
    elif num < menor:
        menor = num

print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))