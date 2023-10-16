from datetime import date

dicionario = {}
anoAtual = date.today().year

nome = input('Informe seu nome: ')
nascimento = int(input('Informe o seu ano de nascimento: '))
carteira = int(input('Digite o número da CTPS: '))

dicionario['nome'] = nome
dicionario['idade'] = anoAtual - nascimento
dicionario['ctps'] = carteira

if carteira != 0:
    contratacao = int(input('Digite o seu ano de contratação: '))
    salario = float(input('Informe o seu salário: '))

    dicionario['contratacao'] = contratacao
    dicionario['salario'] = salario
    dicionario['aposentadoria'] = (anoAtual - nascimento) + (35 - (anoAtual - contratacao))

print('-=' * 35)
print()

for chave in dicionario:
    print('o "{}" tem o valor de "{}"'.format(chave, dicionario[chave]))
