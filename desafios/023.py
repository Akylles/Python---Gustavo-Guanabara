numero = input('Digite um número entre 0 e 9999: ')
numero = int(numero)

milhar = numero // 1000
centena = (numero - milhar * 1000) // 100
dezena = (numero - milhar * 1000 - centena * 100) // 10
unidade = numero - milhar * 1000 - centena * 100 - dezena * 10

print('o número: {}'.format(numero))
print('milhares: {}'.format(milhar))
print('centenas: {}'.format(centena))
print('dezenas: {}'.format(dezena))
print('unidades: {}'.format(unidade))
