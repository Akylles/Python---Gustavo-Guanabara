from random import randint

alunos = []

for i in range(0, 4):
    nomeAluno = input("Digite o nome do aluno: ")
    alunos.insert(i, nomeAluno)

ordemApresentacao = []

for i in range(0, 4):
    posicao = randint(0, 3)
    aluno = alunos[posicao]
    if not (ordemApresentacao.__contains__(aluno)):
        ordemApresentacao.insert(i, aluno)

print('##### --- ORDEM DE APRESENTAÇÃO --- #####')
print(ordemApresentacao)