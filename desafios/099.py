def maior(*numeros):
    print("-=" * 40)
    print("Analisando os valores passados...")

    for valor in numeros:
        print(f'{valor}', end=' ')

    maior = max(numeros)
    qtde = len(numeros)

    print(f'. Foram informados {qtde} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 6, 7, 3, 0, 11, -2)
