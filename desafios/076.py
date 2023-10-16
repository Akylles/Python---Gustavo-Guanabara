produtos = (('sabonete', 1.55), ('ovo', 15.00), ('pasta', 3.75), ('rapadura', 6.30), ('suco', 1.29))

print('Os produtos: {}'.format(produtos))

print('\t##### COMPRAS #####\n')
print('"NOME"...................."PREÇO":')

for prod in produtos:
    print('{}.................... R$ {}'.format(prod[0], prod[1]))