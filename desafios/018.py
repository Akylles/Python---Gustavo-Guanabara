import math

angulo = float(input('Digite o ângulo: '))
angulo = math.radians(angulo)

seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print('Seno: {:.2f}'.format(seno))
print('Cosseno: {:.2f}'.format(cosseno))
print('Tangente: {:.2f}'.format(tangente))