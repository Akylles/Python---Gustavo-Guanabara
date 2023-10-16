km = float(input('Digite os km percoriidos: '))
dias = int(input('Digite a quantidade de dias do aluguel: '))

preco = km * 0.15 + dias * 60

print('O preço a pagar pelo aluguel do carro é: R$ {:.2f}'.format(preco))