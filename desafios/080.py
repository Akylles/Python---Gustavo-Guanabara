lista = []

for i in range(0, 5):
    valor = int(input('Digite o {}º valor: '.format(i + 1)))
    if i == 0 or valor < lista[0]:
        lista.insert(0, valor)
    elif valor > lista[-1]:
        lista.append(valor)
    else:
        tamanho = len(lista)
        for j in range(0, tamanho):
            if valor > lista[j] and valor < lista[j + 1] and j + 1 < tamanho:
                lista.insert(j + 1, valor)

print('\nA lista ordenada: {}'.format(lista))
