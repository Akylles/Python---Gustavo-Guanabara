largura = input('Largura (metros): ')
altura = input('Altura (metros): ')

largura = float(largura)
altura = float(altura)

area = largura * altura
litrosTinta = area / 2

print('A área da parede: {:.2f} m²'.format(area))
print('A quantidade litros de tinta: {} L'.format(litrosTinta))