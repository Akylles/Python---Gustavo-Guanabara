valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))
valor4 = int(input('Digite o quarto valor: '))

tupla = (valor1, valor2, valor3, valor4)
pares = []

for n in tupla:
    if n % 2 == 0:
        pares.append(n)

print('A tupla: {}'.format(tupla))
print('Quantidade de ocorrências do número nove: "{}"'.format(tupla.count(9)))

if tupla.__contains__(3):
    print('Posição do primeiro valor três: {}'.format(tupla.index(3)))
else:
    print('\033[1;31;40mO número "3" não aparece em nenhuma posição na tupla\033[m')
if len(pares) > 0:
    print('Números pares: {}'.format(pares))
else:
    print('\033[1;31;40mNão existem números pares na tupla\033[m')
