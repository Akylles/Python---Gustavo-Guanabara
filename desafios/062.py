a1 = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))

n = 1

while n <= 10:
    termo = a1 + (n - 1) * r
    print('a{} = {}'.format(n, termo))
    n += 1

while True:
    termosExtras = int(input('Quantos termos a mais você quer gerar? '))
    if termosExtras == 0:
        break
    termosExtras += n

    while n < termosExtras:
        termo = a1 + (n - 1) * r
        print('a{} = {}'.format(n, termo))
        n += 1

print('\nFIM')
