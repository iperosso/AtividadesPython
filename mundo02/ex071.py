""" CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRONICO. NO INICIO, PERGUNTE
    AO USUARIO QUAL SERÁ O VALOR A SER SACADO (NUM INTEIRO) E O PROGRAMA VAI INFORMAR
    QUANTAS CEDULAS DE CADA VALOR SERÃO ENTREGUES.
    OBS. CONSIDERE QUE O CAIXA POSSUI CEDULAS DE 50, 20, 10 E 1"""

valor = int(input('Qual o valor a ser sacado? R$ '))
result = valor
ced = 50
totalced = 0
while True:
    if result >= ced:
        result -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cedulas de R$ {ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if result == 0:
            break
