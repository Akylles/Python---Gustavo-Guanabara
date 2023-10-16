
primeroValor = int(input('Digite o 1º valor: '))
soma = primeroValor
maior = primeroValor
menor = primeroValor
i = 1

continuar = input('Deseja continuar? [s/n]: ')

while continuar.lower() == "s":
    i += 1
    enesimoValor = int(input('Digite o {}º valor: '.format(i)))
    soma += enesimoValor
    if enesimoValor > maior:
        maior = enesimoValor
    elif enesimoValor < menor:
        menor = enesimoValor

    continuar = input('Deseja continuar? [s/n]: ')

media = soma / i
print('\033[1;31;40mA média dos números digitados é: {:.2f}\033[m'.format(media))
print('\033[1;31;40mA quantidade de números lidos é: {}\033[m'.format(i))
