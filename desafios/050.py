soma = 0

for i in range(0, 6):
    num = input('Informe o {} número inteiro: '.format(i + 1))
    num = int(num)
    if num % 2 == 0:
        soma += num

print('\033[1;31;40mA soma dos números inteiros pares é: {}\033[m'.format(soma))
