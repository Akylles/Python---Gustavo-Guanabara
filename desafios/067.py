while True:
    numero = int(input('Digite um número: '))
    print('##### TABUADA DE {}\n'.format(numero))
    if numero < 0:
        break
    else:
        for i in range(1, 11):
            print('{} x {} = {}'.format(numero, i, numero * i))
            
print('Finalizada a tabuada')