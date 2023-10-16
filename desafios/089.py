turma = list()

while True:
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    aluno = [nome, nota1, nota2]
    turma.append(aluno)

    continuar = input('\nDeseja continuar? ').strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 30)
print('----- > BOLETIM < -----')
print(f'{"CÓDIGO":<8}{"NOME":<8}{"MÉDIA":>8}')

for chave, valor in enumerate(turma):
    nome = valor[0]
    media = (valor[1] + valor[2]) / 2

    print('{:<8}{:<8}{:>8}'.format(chave, nome, media))

print('-=' * 30)

while True:
    codigo = int(input('Digite o código do aluno para detalhar as notas dele (999 encerra): '))
    if codigo == 999:
        break
    if 0 <= codigo < len(turma):
        aluno = turma[codigo]
        print('\nNotas de {} são: {} e {}\n'.format(aluno[0], aluno[1], aluno[2]))
    else:
        print('\033[1;31;40mO código {} que você digitou é inválido.\033[m'.format(codigo))
