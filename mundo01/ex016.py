"""DESAFIO 016
CRIE UM PROGRAMA QUE LEIA UM NUMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA A SUA PORÇÃO INTEIRA"""

from math import trunc

num = float(input('Digite um numero real'))
print('O numero digitado foi {}, e sua porção inteirra é {}'.format(num, trunc(num)))
