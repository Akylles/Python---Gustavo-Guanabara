numero = int(input('Informe o número a ser convertido: '))
base = -1

while base != 4:
    print('\n----- Digte a base -----\n')
    base = input('1. Binário\n'
                 '2. Octal\n'
                 '3. Hexadecimal\n'
                 '4. Sair...\n')
    base = int(base)
    if base == 1:
        print('\033[1;30;41mO número {} em binário é {}\033[m'.format(numero, bin(numero)[2:]))
    if base == 2:
        print('\033[1;30;41mO número {} em octal é {}\033[m'.format(numero, oct(numero)[2:]))
    if base == 3:
        print('\033[1;30;41mO número {} em hexadecimal é {}\033[m'.format(numero, hex(numero)[2:].upper()))
