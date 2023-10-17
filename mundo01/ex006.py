# CRIE UM ALGORITMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E SUA RAIZ QUADRADA.
from math import sqrt
n = int(input('Digite um número'))
d = n * 2
t = n * 3
r = sqrt(n)
print('Você digitou o número {}, o dobro é de {}, o triplo é de {} e a raiz quadrada vale {}'.format(n, d, t, r))
