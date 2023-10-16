from datetime import date


def calcIdade(nascimento):
    anoAtual = date.today().year
    idade = anoAtual - nascimento

    return idade


def analisaVoto(idade):
    resultado = "OBRIGATÓRIO"

    if idade < 16:
        resultado = "NEGADO"
    elif idade < 18 or idade > 65:
        resultado = "OPCIONAL"

    return resultado


anoNascimento = int(input('Digite o ano de nascimento: '))

idade = calcIdade(anoNascimento)
voto = analisaVoto(idade)

print(f'Com {idade} anos. Voto {voto}')
