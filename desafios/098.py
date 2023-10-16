# Declaração de funçoes

def mensagem(inicio, fim, passo):
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} contando de {abs(passo)} em {abs(passo)}')


def progressiva():
    mensagem(1, 10, 1)
    for i in range(1, 11):
        print(f'{i}', end=' ')
    print('\n')


def regressiva():
    mensagem(10, 0, -2)
    for i in range(10, -1, -2):
        print(f'{i}', end=' ')
    print('\n')


def personalizada(inicio, fim, passo):

    if passo == 0:
        if inicio < fim:
            passo = 1
            fim += 1
        else:
            passo = -1
            fim -= 1
    else:
        mensagem(inicio, fim, passo)
        if passo < 0:
            fim -= 1
        else:
            fim += 1

    for i in range(inicio, fim, passo):
        print(f'{i}', end=' ')


def contagem():
    progressiva()
    regressiva()
    print('Agora é a sua vez de personalizar a mensagem')

    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))

    personalizada(inicio, fim, passo)


# Uso das funções

contagem()
