""" FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VARIOS NÚMEROS, UM DE CADA VEZ, 
    PARA CADA VALOR DIGITADO. O PROGRAMA SERÁ INTERROMPIDO QUANDO O NÚMERO 
    SOLICITADO FOR NEGATIVO"""

num = 0
while True:
    num = int(input('Digite o número que você pretende ver a tabuada'))
    if num <= 0:
        break
    for i in range(1, 11):
        print(f'{i:>2} x {num} = {num * i}')
