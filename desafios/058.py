from random import randint
from time import sleep

tentativas = 0

while True:
    aleatorio = randint(0, 10)
    numero = int(input('Digite um número: '))
    print('PROCESSANDO ...')
    sleep(1)
    tentativas += 1
    if numero == aleatorio:
        print("\033[1;30;46mAcertou! O número sorteado foi {}!!!\033[m".format(aleatorio))
        break
    else:
        print('\033[1;31;40mErrou! O número sorteado foi {}!!!\033[m'.format(aleatorio))


print('O número de tentativas foi {}'.format(tentativas))
