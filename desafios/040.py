nota1 = input('Digite a primeira nota: ')
nota2 = input('Digite a segunda nota: ')

nota1 = float(nota1)
nota2 = float(nota2)

media = (nota1 + nota2) / 2

if media < 5:
    print('\033[1;30;41mMédia: {}. Reprovado!\033[m'.format(media))
elif media < 7:
    print('\033[1;30;41mMédia: {}. Vai fazer recuperação!\033[m'.format(media))
else:
    print('\033[1;30;41mMédia: {}. Parabéns!. Você foi aprovado por média!!\033[m'.format(media))