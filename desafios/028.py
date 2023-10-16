from random import randint
from time import sleep

aleatorio = randint(0, 5)

numero = int(input('Digite um número: '))

print('PROCESSANDO ...')
sleep(3)

if numero == aleatorio:
    print("Acertou! O número sorteado foi {}!!!".format(aleatorio))
else:
    print('Errou! O número sorteado foi {}!!!'.format(aleatorio))
