listaNumeros = []

while True:
    num = int(input('Digite um número: '))
    listaNumeros.append(num)
    sair = str(input('Sair? ')).strip().upper()[0]
    print()
    if sair == 'S':
        break

print('\033[1;31;40mA quantidade de números digitados é: "{}"\033[m'.format(len(listaNumeros)))
print('\033[1;31;40mA lista em forma descrescente: "{}"\033[m'.format(sorted(listaNumeros, reverse=True)))
if 5 in listaNumeros:
    print('\033[1;31;40mO número 5 foi digitado e está na lista\033[m')
else:
    print('\033[1;31;40mO número 5 não foi digitado\033[m')
