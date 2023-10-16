listaJogadores = list()

while True:
    dicionario = dict()

    nome = str(input('\nQual o nome do jogador? '))
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

    listaJogadores.append(dicionario)

    print()
    sair = str(input('Quer sair? ')).strip().upper()[0]
    if sair == 'S':
        break

print()
print('-=' * 30)
print()

print(f'{"COD":<8}{"NOME":<12}{"GOLS":<20}{"TOTAL":>8}')

for i in range(0, len(listaJogadores)):
    jogador = listaJogadores[i]
    codigo = i
    nome = jogador['nome']

    listaGols = '['
    for gol in jogador['gols']:
        listaGols += f' "{str(gol)}"'
    listaGols += ' ]'
    totalGols = jogador['total']

    print('{:<8}{:<12}{:<20}{:>8}'.format(codigo, nome, listaGols, totalGols))

print()
print('-=' * 30)
print()

while True:
    codigo = int(input('Digite o código do jogador do qual desejas detalhar dados (999 encerra): '))
    if codigo == 999:
        break
    elif codigo < 0 or codigo >= len(listaJogadores):
        print('\033[1;31;40mERRO! Não existe jogador com o código {}\033[m'.format(codigo))
    else:
        jogador = listaJogadores[codigo]
        print('\n-----> LEVANTAMENTO DO JOGADOR {}.'.format(jogador['nome']))

        for chave, valor in enumerate(jogador['gols']):
            print('\t=> Na partida {}, fez {} gols.'.format(chave + 1, valor))

        print('Foi um total de {} gols.\n'.format(jogador['total']))
