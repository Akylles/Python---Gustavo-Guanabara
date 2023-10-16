def ficha(jogador, gols):
    if jogador == '':
        jogador = '<desconhecido>'
    if gols == '':
        gols = '0'
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


nomeJogador = input('Digite o nome do jogador: ')
numGols = input('Digite a quantidade de gols que ele fez: ')

ficha(nomeJogador, numGols)
