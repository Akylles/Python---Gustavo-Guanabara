i = 0
soma = 0

while True:
    numero = int(input('Digite um número inteiro: '))
    if numero != 999:
        soma += numero
        i += 1
    else:
        break

print('\033[1;33;40mA quantidade de números lidos foi {}\033[m'.format(i))
print('\033[1;33;40mA soma total dos números lidos foi {}\033[m'.format(soma))