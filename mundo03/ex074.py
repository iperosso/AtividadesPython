# CRIE UM PROGRAMA QUE VAI GERAR CINCO NÚMEROS ALEATORIOS E COLOCAR EM UMA TUPLA.
# DEPOIS DISSO, MOSTRE A LISTAGEM DOS NÚMEROS GERADOS E TAMBÉM INDIQUE O MENOR E MAIOR VALOR
# QUE ESTÃO NA TUPLA
from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números sorteados foram {num}')
print(f'O maior é {max(num)} e o menor é {min(num)}')
