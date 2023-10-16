from datetime import date

anoNascimento = input('Digite o ano de seu nascimento: ')
anoNascimento = int(anoNascimento)
anoAtual = date.today().year
idade = anoAtual - anoNascimento

if idade <= 9:
    print('\033[1;31;40mMIRIM\033[m. Idade = {}'.format(idade))
elif idade <= 14:
    print('\033[1;31;40mINFANTIL\033[m. Idade = {}'.format(idade))
elif idade <= 19:
    print('\033[1;31;40mJÚNIOR\033[m. Idade = {}'.format(idade))
elif idade <= 20:
    print('\033[1;31;40mSÊNIOR\033[m. Idade = {}'.format(idade))
else:
    print('\033[1;31;40mMASTER\033[m. Idade = {}'.format(idade))
