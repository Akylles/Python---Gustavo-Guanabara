from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('A tupla: {}'.format(numeros))
print('O menor valor: {}'.format(min(numeros)))
print('O maior valor: {}'.format(max(numeros)))
