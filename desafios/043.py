peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Abaixo do peso. IMC = {:.2f}'.format(imc))
elif imc <= 25:
    print('Peso ideal. IMC = {:.2f}'.format(imc))
elif imc <= 30:
    print('Sobrepeso. IMC = {:.2f}'.format(imc))
elif imc <= 40:
    print('Obesidade. IMC = {:.2f}'.format(imc))
else:
    print('Obesidade mórbida. IMC = {:.2f}'.format(imc))
