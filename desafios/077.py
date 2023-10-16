tuplaPalavras = ('ronaldo', 'rivaldo', 'ronaldinho', 'cafu', 'marcos', 'lucio')
tuplaVogais = 'aeiou'

for palavra in tuplaPalavras:
    vogais = []
    for letra in palavra:
        if letra in tuplaVogais:
            vogais.append(letra)
    print("As vogais presentes na palavra '{}' são {}".format(palavra.upper(), vogais))
    vogais = []

