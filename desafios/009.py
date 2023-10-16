numero = int(input('Informe um número natural: '))

while numero <= 0:
    numero = int(input('Informe um número natural: '))
else:
    print('\n#### -- Tabuada -- #####\n')


print('--> Soma\n')


for i in range(1, 11):
    resultado = numero + i
    if resultado >= 0:
        print('{} + {} = {}'.format(numero, i, resultado))
    

print('\n-- > Subtração\n')


for i in range(1, 11):
    resultado = numero - i
    if resultado >= 0:
        print('{} - {} = {}'.format(numero, i, resultado))
    

print('\n-- > Multiplicação\n')


for i in range(1, 11):
    resultado = numero * i
    print('{} x {} = {}'.format(numero, i, resultado))

print('\n-- > Divisão\n')


for i in range(1, 11):
    resultado = numero // i
    print('{} / {} = {}'.format(numero, i, resultado))