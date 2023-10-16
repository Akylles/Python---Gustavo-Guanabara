num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:
    print('\033[1;32;40mO primeiro número é maior\033[m')
elif num1 < num2:
    print('\033[1;32;40mO segundo número é maior\033[m')
else:
    print('\033[1;32;40mOs número são iguais\033[m')
