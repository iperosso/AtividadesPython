"""DESAFIO 013
ESCREVA UM PROGRAMA QUE LEIA O SALARIO DE UM FUNCIONÁRIO E MOSTRE-O COM UM REAJUSTE DE AUMENTO DE 5%"""

sal = float(input('Digite o valor do salário atual'))
aum = sal + (sal / 100 * 15)
print('Com o reajuste o funcionário passará a receber R${}'.format(aum))
