numero = input('Digite um número inteiro: ')
numero = int(numero)

resultado = 'ÍMPAR'

if numero % 2 == 0:
    resultado = 'PAR'

print('O número {} é {}'.format(numero, resultado))