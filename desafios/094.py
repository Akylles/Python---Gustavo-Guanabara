lista = list()
mulheres = list()
somaIdades = 0

while True:
    nome = input('Digite o nome: ')
    sexo = input('Digite o sexo: ').strip().upper()[0]
    idade = int(input('Idade: '))

    somaIdades += idade

    dicionario = {'nome': nome, 'sexo': sexo, 'idade': idade}

    if sexo == 'F':
        mulheres.append(dicionario['nome'])

    lista.append(dicionario)

    sair = input('\nQuer sair? ').strip().upper()[0]
    if sair == 'S':
        break

    print()
    print('-=' * 30)

media = somaIdades / len(lista)

acimaMedia = list()

for pessoa in lista:
    if pessoa['idade'] > media:
        acimaMedia.append(pessoa)

print('-=' * 30)
print()

print('Quantidade de pessoas cadastradas: "{}".'.format(len(lista)))
print('A média de idade é: "{:.2f}" anos.'.format(media))
print('As mulheres cadastradas são: {}'.format(mulheres))
print('A pessoas com idade acima da média são: ')

for pessoa in acimaMedia:
    print(pessoa)