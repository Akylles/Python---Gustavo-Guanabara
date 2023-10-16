def area(lar, alt):
    return lar * alt


print('-' * 30)
print('Controle de terrenos\n')

largura = input('Informe a largura: ')
altura = input('Informe a altura: ')

largura = float(largura)
altura = float(altura)

print(f'A área do terreno {largura} x {altura} é {area(largura, altura):.3f}')
