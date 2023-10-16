from datetime import date

ano = input('Infome o ano: ')
ano = int(ano)

if ano == 0:
    ano = date.today().year
    print('Ano atual: {}'.format(ano))

bissexto = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
print('O ano de {} é bissexto? {}'.format(ano, bissexto))
