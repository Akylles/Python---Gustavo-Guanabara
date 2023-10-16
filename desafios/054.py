import datetime
anoAtual = datetime.date.today().year

maiores = 0
menores = 0

for i in range(0, 6):
    nascimento = input('Digite o seu ano de nascimento: ')
    nascimento = int(nascimento)
    idade = anoAtual - nascimento

    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print('{} pessoas maiores de idade e {} pessoas menores de idade'.format(maiores, menores))
