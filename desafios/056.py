somatorio = 0
maiorIdade = 0
mulheres = 0
nomeMaiorIdade = ''

for i in range(0, 4):
    print('##### LEITURA DE DADOS #####\n')
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo: ')

    somatorio += idade
    if idade > maiorIdade and sexo.upper() == 'M':
        maiorIdade = idade
        nomeMaiorIdade = nome
    if sexo.upper() == 'F' and idade < 20:
        mulheres += 1

    print()

media = somatorio / 4

print('A média de idade é: {}'.format(media))
print('O homem mais idoso é {} e possui {} anos.'.format(nomeMaiorIdade, maiorIdade))
print('Existem {} mulheres com menos de 20 anos.'.format(mulheres))
