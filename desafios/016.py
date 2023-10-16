from math import trunc

numero = float(input('Digite um número: '))
parteInteira = trunc(numero)

print('A parte inteira do número {} é {}'.format(numero, parteInteira))