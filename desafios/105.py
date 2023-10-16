def notas(* n, sit=False):
    """
    Função para analisar notas e situação de um aluno
    :param n:
        Uma ou mais notas do aluno.
    :param sit:
        Valor booleano para mostrar a situação ou não
    :return:
        Um dicionário com as informações a respeito das notas
    """
    qtde = len(n)
    menor = min(n)
    maior = max(n)
    media = sum(n) / qtde

    dicionario = {
        'Qtde Notas': qtde,
        'Menor Nota': menor,
        'Maior Nota': maior,
        'Media': round(media, 2)
    }
    if sit:
        situacao = 'BOA'
        if media <= 4:
            situacao = 'RUIM'
        elif media < 7:
            situacao = 'REGULAR'
        dicionario['Situação'] = situacao
    return dicionario


print(notas(7, 10, 9, 4, sit=True))
help(notas)
