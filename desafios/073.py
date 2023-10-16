times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Grêmio', 'Fluminense', 'Atlético-MG', 'São Paulo', 'Cruzeiro',
         'Fortaleza', 'Bahia', 'Ceará', 'Sport', 'Chapecoense', 'Corinthias', 'Santos', 'Internacional',
         'Vasco', 'América-MG', 'Goiás', 'Portuguesa')

print('-=' * 15)
print('Os 5 primeiros colocados: {}'.format(times[:5]))
print('A zona de rebaixamento: {}'.format(times[-4:]))
print('Os times em ordem alfabética: {}'.format(sorted(times)))
print('A posição do time "Chapecoense é: {}'.format(times.index('Chapecoense') + 1))
print('-=' * 15)
