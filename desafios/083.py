parenteseAberto = 0

expressao = str(input('Digite a expressão: '))

for caractere in expressao:
    if caractere == '(':
        parenteseAberto += 1
    elif caractere == ')':
        parenteseAberto -= 1
        if parenteseAberto < 0:
            break

if parenteseAberto == 0:
    print('\033[1;31;40mA expressão está correta\033[m')
else:
    print('\033[1;31;40mA expressão NÃO está correta\033[m')
