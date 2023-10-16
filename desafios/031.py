distancia = input('Digite a distância da viagem em km: ')
distancia = float(distancia)

preco = distancia * 0.5

if distancia > 200:
    preco = distancia * 0.45

print('O preço pela viagem é de R$ {:.2f}'.format(preco))