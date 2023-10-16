nome = input('Digite o nome: ')
media = float(input('Digite a média: '))

if media >= 7:
    situacao = 'aprovado'
elif 4 <= media < 7:
    situacao = 'recuperacao'
else:
    situacao = 'reprovado'

aluno = {'nome': nome, 'media': media, 'situacao': situacao}

print('-=' * 20)

print('O nome é {}, a média é {:.1f} e a situação é {}'.format(aluno['nome'], aluno['media'], aluno['situacao']))
