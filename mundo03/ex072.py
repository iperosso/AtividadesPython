""" CRIE UM PROGRAMA COM UMA TUPLA TOTALMENTE PREENCHIDA COM UMA CONTAGEM POR EXTENSO 
    DE ZERO A VINTE. SEU PROGRAMA DEVERÁ LER UM NÚMERO PELO TECLADO (ENTRE 0 E 20) E MOSTRA-LO
    POR EXTENSO """

regist = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
indice = int(input('Digite um número de 0 a 20: '))
print(f'O número {indice} por extenso é {regist[indice].capitalize()}')
