dicionario = dict()

nome = str(input('Qual o nome do jogador? '))
partidas = int(input('Quantas partidas ele jogou? '))

print('-=' * 30)

aproveitamento = list()
total = 0

for i in range(0, partidas):
    gols = int(input('Quantos gols {} fez na partida {}: '.format(nome, i + 1)))
    total += gols
    aproveitamento.append(gols)

dicionario['nome'] = nome
dicionario['gols'] = aproveitamento
dicionario['total'] = total

print()
print('-=' * 30)
print()

for campo in dicionario:
    print('O campo "{}" tem o valor de "{}"'.format(campo, dicionario[campo]))

print()
print('-=' * 30)
print()

print('O jogador {} jogou {} partidas.'.format(nome, partidas))

for chave, valor in enumerate(dicionario['gols']):
    print('\t=> Na partida {}, fez {} gols.'.format(chave + 1, valor))

print('Foi um total de {} gols.'.format(dicionario['total']))
