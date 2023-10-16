valorCasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do salário: '))
anos = int(input('Em quantos anos você planeja pagar a casa? '))

prestacaoMax = salario * 0.3
valorPrestacao = valorCasa / (anos * 12)

print('Valor da prestação: \033[1;34m{:.2f}\033[m'.format(valorPrestacao))

if valorPrestacao <= prestacaoMax:
    print('\033[1;32;40mEmpréstimo autorizado!\033[m')
else:
    print('\033[1;31;40mEmpréstimo negado, pois a prestação não pode exceder 30% do salário\033[m!')
