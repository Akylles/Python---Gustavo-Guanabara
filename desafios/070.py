gastosTotais = 0
maioresQueMil = 0
maisBarato = 0
nomeMaisBarato = ''

while True:
    print('-----> NOVO PRODUTO <-----\n')

    nomeProduto = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o preço do produto: '))

    if gastosTotais == 0:
        maisBarato = preco
        nomeMaisBarato = nomeProduto
    elif preco < maisBarato:
        maisBarato = preco
        nomeMaisBarato = nomeProduto
    if preco > 1000:
        maioresQueMil += 1
    gastosTotais += preco

    continuar = str(input('Deseja continuar [S/n] ? ')).strip().upper()

    print()

    if continuar == 'N':
        break


print('\033[1;31;40mOs gastos totais com compras são {:.2f}\033[m'.format(gastosTotais))
print('\033[1;31;40mA quantidade de produtos que custam mais que R$ 1000 é {}'.format(maioresQueMil))
print('\033[1;31;40mO nome do produto mais barato é "{}"'.format(nomeMaisBarato))
