def leiaInt():
    try:
        numero = int(input('Digite um número: '))
        print(f'Você digitou o número {numero}')
    except:
        print('\033[1;31;40mValor inválido. Por favor digite um número inteiro\033[m')


leiaInt()
