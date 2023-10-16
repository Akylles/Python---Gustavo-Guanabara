peso = input('Digite o peso da 1-ésima pessoa: ')
maior = float(peso)
menor = maior

for i in range(2, 6):
    peso = input('Digite o peso da {}-ésima pessoa: '.format(i))
    peso = float(peso)

    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('\033[1;31;40mMaior peso: {:.2f}\033[m'.format(maior))
print('\033[1;31;40mMenor peso: {:.2f}\033[m'.format(menor))
