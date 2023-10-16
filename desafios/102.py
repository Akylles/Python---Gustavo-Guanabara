def fatorial(num = 1, show=False):
    """
        Calcula o fatoria de um número
    :param num:
        o número do qual deve ser calculado o fatorial
    :param show:
        valor booleano que indica se o processo de cálculo deve ser exibido
    :return:
        o valor do fatorial de num
    """
    resultado = 1

    for i in range(num, 0, -1):
        if show:
            if i == 1:
                print(f'{i}', end=' = ')
            else:
                print(f'{i}', end=' x ')
        resultado *= i
    if show:
        print(resultado)

    return resultado


f = fatorial(6)

print(f'O fatorial de {3} é {f}')
help(fatorial)
