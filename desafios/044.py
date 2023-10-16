precoNormal = float(input('Digite o preço do produto: '))

aVistaDinheiroCheque = precoNormal * 0.9
aVistaCartao = precoNormal * 0.95
duasVezesCartao = precoNormal
tresVezesCartao = precoNormal * 1.2

menu = ('\n##### INFORME A CONDIÇÃO DE PAGAMENTO #####\n'
        '1. À vista no dinheiro ou cheque\n'
        '2. À vista no cartão\n'
        '3. Duas vezes no cartão\n'
        '4. Três vezes no cartão ou mais\n'
        'Digite a opção: ')

opcao = int(input(menu))

if opcao == 1:
    print('\n\033[1;31;40mValor a ser pago: {:.2f}\033[m'.format(aVistaDinheiroCheque))
elif opcao == 2:
    print('\n\033[1;31;40mValor a ser pago: {:.2f}\033[m'.format(aVistaCartao))
elif opcao == 3:
    print('\n\033[1;31;40mValor a ser pago: {:.2f}\033[m'.format(duasVezesCartao))
elif opcao == 4:
    print('\n\033[1;31;40mValor a ser pago: {:.2f}\033[m'.format(tresVezesCartao))
