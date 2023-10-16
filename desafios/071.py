valor = int(input('Informe o valor a ser sacado: '))

cinquenta = valor // 50
vinte = (valor - cinquenta * 50) // 20
dez = (valor - cinquenta * 50 - vinte * 20) // 10
um = valor - cinquenta * 50 - vinte * 20 - dez * 10

print('Cédulas de R$ 50: {}'.format(cinquenta))
print('Cédulas de R$ 20: {}'.format(vinte))
print('Cédulas de R$ 10: {}'.format(dez))
print('Cédulas de R$ 1: {}'.format(um))
