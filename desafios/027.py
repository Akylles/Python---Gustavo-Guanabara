nome = str(input("Digite seu nome completo: "))
nome = nome.strip()
listaNomes = nome.split()

print("Primeiro nome: {}".format(listaNomes[0]))
print("Último nome: {}".format(listaNomes[len(listaNomes) - 1]))