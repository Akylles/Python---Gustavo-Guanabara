from random import randint
from time import sleep
from operator import itemgetter

jogadas = dict()

for i in range(1, 5):
    aleatorio = randint(1, 6)
    jogadas[f'jogador0{i}'] = aleatorio

ordenaPorValor = sorted(jogadas.items(), key=itemgetter(1))
maiorValor = ordenaPorValor[-1][1]
vencedores = list()

for nome in jogadas:
    if jogadas[nome] == maiorValor:
        vencedores.append(nome)

print('-=' * 30)
print()
print('Jogadas em ordem crescente: {}'.format(ordenaPorValor))
print('O(s) vencedor(es) foram "{}"'.format(vencedores))
