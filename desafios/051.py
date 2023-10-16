a1 = int(input('Infome o primeiro termo da P.A: '))
razao = int(input('Informe a razão da P.A: '))

for i in range(1, 11):
    termo = a1 + (i - 1) * razao
    print('O {}º termo: {}'.format(i, termo))

