frase = input('Digite a frase: ')

novaFrase = ''

for i in range(0, len(frase)):
    if frase[i] != ' ':
        novaFrase += frase[i]

inverso = ''

for i in range(len(frase) - 1, -1, -1):
    if frase[i] != ' ':
        inverso += frase[i]

if novaFrase == inverso:
    print('É palíndromo.')
else:
    print('Não é palíndromo')
