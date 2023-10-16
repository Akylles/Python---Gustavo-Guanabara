matriz = [[], [], []]

for i in range(0, 3):
    print('###### LINHA {} #####'.format(i + 1))
    for j in range(0, 3):
        valor = int(input('Digite o valor da posição [{}][{}]: '.format(i + 1, j + 1)))
        matriz[i].append(valor)
    print()

print('-=' * 40)

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[i][j]} ]', end=' ')
    print()
