import math

catetoOposto = input('Digite o cateto oposto: ')
catetoAdjacente = input('Digite o cateto adjacente: ')

catetoOposto = float(catetoOposto)
catetoAdjacente = float(catetoAdjacente)

quadradoDosCatetos = math.pow(catetoAdjacente, 2) + math.pow(catetoOposto, 2)

hipotenusa = math.sqrt(quadradoDosCatetos)

print("A hipotenusa é igual a {:.2f}".format(hipotenusa))