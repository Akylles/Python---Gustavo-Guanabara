from random import randint

while True:
    print('------ VAMOS JOGAR PAR OU ÍMPAR ------')
    opcao = input('Vocẽ quer par ou ímpar? ').strip().upper()
    jogador = int(input('Digite um número: '))
    maquina = randint(1, 5)

    if (maquina + jogador) % 2 == 0:
        if opcao == 'PAR':
            print('\n\033[1;31;40mVocê venceu!!!\033[m')
            print('\033[1;31;40mVocê jogou {}, a máquina {}. '
                  'A soma é {} que é PAR!!!\033[m'.format(jogador, maquina, maquina + jogador))
        elif opcao == 'IMPAR':
            print('\n\033[1;31;40mA máquina venceu!!!\033[m')
            print('\n\033[1;31;40mVocê jogou {}, a máquina {}. '
                  'A soma é {} que é PAR!!!\033[m'.format(jogador, maquina, maquina + jogador))
            break
    else:
        if opcao == 'IMPAR':
            print('\n\033[1;31;40mVocê venceu!!!\033[m')
            print('\033[1;31;40mVocẽ jogou {}, a máquina {}. '
                  'A soma é {} que é ÍMPAR!!!\033[m'.format(jogador, maquina, maquina + jogador))
        elif opcao == 'PAR':
            print('\n\033[1;31;40mA máquina venceu!!!\033[m')
            print('\033[1;31;40mVocê jogou {}, a máquina {}. '
                  'A soma é {} que é ÍMPAR!!!\033[m'.format(jogador, maquina, maquina + jogador))
            break
