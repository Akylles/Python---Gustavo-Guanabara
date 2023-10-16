salario = input('Digite o seu salário: ')
salario = float(salario)

aumento = salario * 0.15

if salario > 1250:
    aumento = salario * 0.10

print('Você receberá um aumento de R$ {:.2f}. '
      'Seu novo salário será de R$ {:.2f}'.format(aumento, salario + aumento))
