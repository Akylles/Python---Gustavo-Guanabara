frase = input('Digite a frase: ')
frase = frase.strip()
frase = frase.lower()

print('Quantas vezes aparece a letra "a": {}'.format(frase.count('a')))
print('Primeira vez que aparece a letra "a": {}'.format(frase.find('a')))
print('Última vez que aparece a letra "a": {}'.format(frase.rfind('a')))
