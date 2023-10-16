valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

if valor1 > valor2:
    maior = valor1
else:
    maior = valor2

menu = ('[ 1 ] Somar\n'
        '[ 2 ] Multiplicar\n'
        '[ 3 ] Maior\n'
        '[ 4 ] Novos números\n'
        '[ 5 ] Sair do programa\n')

resposta = 0

while resposta != 5:
    resposta = int(input(menu))

    if resposta == 1:
        print('\n\033[1;30;45mA soma é: {}\033[m\n'.format(valor1 + valor2))
    if resposta == 2:
        print('\n\033[1;30;45mA multiplicação é: {}\033[m\n'.format(valor1 * valor2))
    if resposta == 3:
        print('\n\033[1;30;45mO maior número é: {}\033[m\n'.format(maior))
    if resposta == 4:
        valor1 = float(input('Digite o primeiro valor: '))
        valor2 = float(input('Digite o segundo valor: '))

        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2

print('\nFIM')