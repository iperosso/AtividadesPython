""" FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA PARA O ESTOURO DE
    FOGOS DE ARTIFÍCIO, INDO DE 10 A 0, COM UMA PAUSA DE 1 SEGUNDO ENTRE ELES"""
from time import sleep
for n in range(10, 0, -1):
    print(n)
    sleep(1)
print('Feliz Ano novo')
