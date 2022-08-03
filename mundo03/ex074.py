""" CRIE UM PROGRAMA QUE VAI GERAR CINCO NÚMEROS ALEATORIOS E COLOCAR EM UMA TUPLA.
    DEPOIS DISSO, MOSTRE A LISTAGEM DOS NÚMEROS GERADOS E TAMBÉM INDIQUE O MENOR E MAIOR VALOR
    QUE ESTÃO NA TUPLA"""

from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
menor = maior = 0
print(num)
for i in range(0, len(num)):
    if menor == 0:
        menor = num[0]
        maior = num[0]
    elif num[i] < menor:
        menor = num[i]
    elif num[i] > maior:
        maior = num[i]
print(f'O maior é {maior} e o menor é {menor}')
