# DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS E DIGA AO USUARIO SE ELAS
# PODEM OU NÃO FORMAR UM TRIÂNGULO.
from time import sleep
print('=+=' * 10)
print('   Analisador de Triângulo')
print('=+=' * 10)
a = float(input('Qual a primeira medida? '))
b = float(input('Qual a segunda medida? '))
c = float(input('Qual a terceira medida? '))
print('Analisando...')
sleep(3)
if a + b >= c and b + c >= a and a + c >= b:
    print('Essas medidas formam um triângulo!')
else:
    print('Essas medidas NÃO formam um triângulo!')
