from random import randint

jogo = ['pedra', 'papel', 'tesoura']

numeroSorteado = randint(0, 2)
print(numeroSorteado + 1)

menu = ('##### JOGO DA PEDRA PAPEL E TESOURA #####\n'
        '1. Pedra\n'
        '2. Papel\n'
        '3. Tesoura\n'
        'Digite a opção: ')

opcao = int(input(menu)) - 1

maquina = jogo[numeroSorteado]
usuario = jogo[opcao]

if maquina == usuario:
    print('\033[1;31;40mEMPATE!\033[m')
elif (maquina == 'pedra' and usuario == 'tesoura' or maquina == 'tesoura' and usuario == 'papel'
      or maquina == 'papel' and usuario == 'pedra'):
    print('\033[1;30;45mMáquina: {}, Usuário: {}\033[m'.format(maquina, usuario))
    print('\033[1;31;40mVitória da máquina\033[m')
elif (usuario == 'pedra' and maquina == 'tesoura' or usuario == 'tesoura' and maquina == 'papel'
      or usuario == 'papel' and maquina == 'pedra'):
    print('\033[1;30;45mUsuário: {}, Máquina: {}\033[m'.format(maquina, usuario))
    print('\033[1;31;40mVitória do usuário\033[m')
