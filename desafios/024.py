cidade = str(input("Digite o nome da cidade: "))
cidade = cidade.strip()
comecaComSanto = cidade.lower().startswith("santo")
print('Começa com SANTO?: {}'.format(comecaComSanto))