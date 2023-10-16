a = float(input('Digite o lado "a" do triângulo: '))
b = float(input('Digite o lado "b" do triângulo: '))
c = float(input('Digite o lado "c" do triângulo: '))

if ((abs(b - c) < a) and (a < b + c)) and ((abs(a - c) < b) and (b < a + c)) and ((abs(a - b) < c) and (c < a + b)):
    if a == b and b == c:
        print('Forma triângulo \033[1;31;40mEQUILÁTERO.\033[m')
    elif a == b and b != c or a != b and b == c or a == c and c != b:
        print('Forma triângulo \033[1;31;40mISÓSCELES.\033[m')
    else:
        print('Forma triângulo \033[1;31;40mESCALENO.\033[m')
else:
    print('Não forma triângulo.')
