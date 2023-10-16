import random

alunos = []

for i in range(0, 4):
    nomeAluno = input('Dgite o nome do aluno {}: '.format(i + 1))
    alunos.insert(i, nomeAluno)

posicaoSorteada = random.randint(0, 3)

alunoSorteado = alunos[posicaoSorteada]

print('O aluno sorteado foi {}'.format(alunoSorteado))
