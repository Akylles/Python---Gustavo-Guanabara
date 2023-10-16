soma = 0
i = 0

while True:
    entrada = int(input('Informe o número: '))

    if entrada == 999:
        break
    else:
        soma += entrada
        i += 1

print('\033[1;31;40mA soma dos números digitados é: {}\033[m'.format(soma))
print('\033[1;31;40mA quantidade de números lidos é: {}\033[m'.format(i))
