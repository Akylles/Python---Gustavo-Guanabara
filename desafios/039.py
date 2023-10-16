import datetime

anoNascimento = int(input('Digite o seu ano de nascimento: '))
anoAtual = datetime.date.today().year
idade = anoAtual - anoNascimento

if idade == 18:
    print('\033[4;30;47m{} anos.\033[m \033[1:31:40mEstá na hora de se alistar\033[m'.format(idade))
elif idade < 18:
    tempo = 18 - idade
    print('\033[4;30;47m{} anos.\033[m \033[1:31:40mFalta(m) {} ano(s) pro seu alistamento\033[m'.format(idade, tempo))
else:
    tempo = idade - 18
    print('\033[4;30;47m{} anos.\033[m \033[1:31:40mAlistamento deveria ter sido feito há {} ano(s)\033[m'.format(idade, tempo))



