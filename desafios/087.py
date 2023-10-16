matriz = [[], [], []]
pares = 0
terceiraColuna = 0
maiorSegundaLinha = 0

for i in range(0, 3):
    print('###### LINHA {} #####'.format(i + 1))
    for j in range(0, 3):
        valor = int(input('Digite o valor da posição [{}][{}]: '.format(i + 1, j + 1)))
        matriz[i].append(valor)
        if valor % 2 == 0:
            pares += valor
        if j == 2:
            terceiraColuna += valor
        if i == 1:
            if j == 0:
                maiorSegundaLinha = valor
            elif valor > maiorSegundaLinha:
                maiorSegundaLinha = valor
    print()

print('-=' * 35)

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[i][j]} ]', end=' ')
    print()

print('-=' * 35)

print('A soma de todos os valores pares é: {}'.format(pares))
print('A soma de todos os valores da terceira coluna é: {}'.format(terceiraColuna))
print('O maior valor da segunda linha é: {}'.format(maiorSegundaLinha))
