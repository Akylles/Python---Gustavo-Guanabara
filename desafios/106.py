def mensagem():
    print('\033[1;30;42m-=' * 30)
    print('  SISTEMA DE AJUDA PyHELP')
    print('-=' * 30)


def manual(comando):
    print('\033[1;30;46m-=' * 30)
    print(f'  Acessando o manual do comando {comando}')
    print('-=' * 30)
    print('\033[m')
    help(comando)


while True:
    mensagem()
    comando = str(input('\033[mFunção ou biblioteca: '))
    if comando.upper() == 'FIM':
        print('\033[1;30;41m-=' * 30)
        print(f'  ATÉ LOGO')
        print('-=' * 30)
        break
    manual(comando)
