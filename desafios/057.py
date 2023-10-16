sexo = input('Digite o sexo (M/F): ').strip()
sexo = sexo.upper()

while sexo != 'M' and sexo != 'F':
    print('\033[1;31;40mSEXO INVÁLIDO. DIGITE NOVAMENTE...\033[m')
    sexo = input('Digite o sexo (M/F): ').strip()
    sexo = sexo.upper()

print('FIM')