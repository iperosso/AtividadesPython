""" REFAÇA O DESAFIO 035 DOS TRIANGULOS, ACRESCENTANDO O RECURSO DE MOSTRAR QUE TIPO DE
    TRIANGULO SERÁ FORMADO:
    >EQUILÁTERO: TODOS OS LADOS IGUAIS
    >ISOCELES: DOIS LADOS IGUAIS E UM DIFERENTE
    >ESCALENO: TODOS OS LADOS DIFERENTES"""
from time import sleep
print('=+=' * 15)
print('Analisador de triangulo')
print('=+=' * 15)
m1 = float(input('Qual a primeira medida? '))
m2 = float(input('Qual a segunda medida? '))
m3 = float(input('Qual a terceira medida? '))
print('Analisando...')
sleep(3)
if m1 + m2 >= m3 and m2 + m3 >= m1 and m1 + m3 >= m2:
    if m1 != m2 and m2 != m3 and m1 != m3:
        print('Esse é um triangulo ESCALENO')
    elif m1 == m2 and m2 == m3:
        print('Esse é um triangulo EQUILATERO')
    else:
        print('Esse é um triangulo ISOCELES')
else:
    print('Essas medidas não formam um triangulo')
