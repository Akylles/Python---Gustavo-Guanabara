lista = []

for i in range(0, 5):
    valor = float(input('Digite o {}º valor: '.format(i + 1)))
    lista.append(valor)

maior = max(lista)
menor = min(lista)

posicoesMaior = []
posicoesMenor = []

for chave, valor in enumerate(lista):
    if valor == maior:
        posicoesMaior.append(chave)
    elif valor == menor:
        posicoesMenor.append(chave)

print('\nO maior valor digitado foi "{:.2f}" e ocupa a(s) posição(es) "{}"'.format(maior, posicoesMaior))
print('O menor valor digitado "{:.2f}" e ocupa a(s) posição(es) "{}"'.format(menor, posicoesMenor))
