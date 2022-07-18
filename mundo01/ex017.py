"""DESAFIO 017
FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIANGULO RETANGULO
CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA"""

from math import hypot

co = float(input('Digite o valor do Cateto Oposto'))
ca = float(input('Digite o valor do Cateto Adjacente'))
hypo = hypot(co, ca)
print('Com o Cateto Oposto de {}, e o Cateto Adjacente de {}, a Hipotenusa irá valer {:.2f}'.format(co, ca, hypo))
