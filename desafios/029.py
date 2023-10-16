velocidade = input('Digite a velocidade em km/h: ')
velocidade = float(velocidade)

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi multado em R$ {:.2f}'.format(multa))
else:
    print('Parabéns. Você não foi multado.')