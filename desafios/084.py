pessoas = list()
magras = list()
gordas = list()
menorPeso = 0
maiorPeso = 0

while True:
    print('-=' * 30)
    nome = str(input('Nome? '))
    peso = float(input('Peso? '))
    pessoa = [nome, peso]

    if len(pessoas) == 0:
        menorPeso = peso
        maiorPeso = peso
    else:
        if peso <= menorPeso:
            menorPeso = peso
        elif peso >= maiorPeso:
            maiorPeso = peso

    pessoas.append(pessoa[:])

    sair = str(input('\nContinuar cadastrando? ')).strip().upper()[0]
    print()
    if sair == 'N':
        break

for p in pessoas:
    if p[1] == maiorPeso:
        gordas.append(p[0])
    elif p[1] == menorPeso:
        magras.append(p[0])

print('\033[1;31;40mA quantidade de pessoas cadastradas: "{}"'.format(len(pessoas)))
print('\033[1;31;40mO maior peso é {}. A(s) pessoa(s) mais pesadas são: {}'.format(maiorPeso, gordas))
print('\033[1;31;40mO menor peso é {}. A(s) pessoa(s) mais leves são: {}'.format(menorPeso, magras))
