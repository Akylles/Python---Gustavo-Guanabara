n = int(input('Digite um número inteiro: '))

print('##### FIBONACCI #####\n')

ant = 1
suc = 1
fib = 1
i = 1

while i <= n:
    if i <= 2:
        print('{}º termo = {}'.format(i, fib))
    else:
        fib = ant + suc
        print('{}º termo = {}'.format(i, fib))
        ant = suc
        suc = fib
    i += 1

print('\nFIM')
