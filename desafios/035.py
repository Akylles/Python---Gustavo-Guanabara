a = int(input('Digite o lado "a" do triângulo: '))
b = int(input('Digite o lado "b" do triângulo: '))
c = int(input('Digite o lado "c" do triângulo: '))

# | b - c | < a < b + c
# | a - c | < b < a + c
# | a - b | < c < a + b

if ((abs(b - c) < a) and (a < b + c)) and ((abs(a - c) < b) and (b < a + c)) and ((abs(a - b) < c) and (c < a + b)):
    print('Forma triângulo.')
else:
    print('Não forma triângulo.')