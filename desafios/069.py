acima18 = 0
homens = 0
mulheresMenos20 = 0

while True:
    idade = int(input('Informe a idade: '))
    if idade > 18:
        acima18 += 1
    sexo = input('Informe o sexo [M/f]: ').strip().upper()
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheresMenos20 += 1

    continuar = input('Desejas continuar? [S/n] ').strip().upper()
    print()
    
    if continuar == 'N':
        break

print('\033[1;31;40mO número de pessoas acima de 18 anos é: {}\033[m'.format(acima18))
print('\033[1;31;40mA quantidade de homens é: {}\033[m'.format(homens))
print('\033[1;31;40mA quantidade de mulheres com menos de 20 anos é: {}\033[m'.format(mulheresMenos20))
