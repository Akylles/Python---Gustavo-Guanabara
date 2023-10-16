numero = input('Digite um número inteiro: ')
numero = int(numero)

qtdeDivisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        qtdeDivisores += 1

if qtdeDivisores == 2:
    print('O número {} é primo.'.format(numero))
else:
    print('O número {} NÃO é primo.'.format(numero))
