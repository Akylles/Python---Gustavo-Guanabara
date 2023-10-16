from random import randint
from time import sleep

megasena = list()
numJogos = int(input('Informe quantos jogos serão gerados: '))

for i in range(0, numJogos):
    jogo = list()

    j = 0
    while j < 6:
        aleatorio = randint(1, 60)
        if aleatorio not in jogo:
            jogo.append(aleatorio)
            j += 1

    jogo.sort()
    megasena.append(jogo[:])

print('-=' * 30)

for i, mega in enumerate(megasena):
    print(f"JOGO {i + 1}: {mega}")
    sleep(1)
