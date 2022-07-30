""" CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRONICO. NO INICIO, PERGUNTE
    AO USUARIO QUAL SERÁ O VALOR A SER SACADO (NUM INTEIRO) E O PROGRAMA VAI INFORMAR
    QUANTAS CEDULAS DE CADA VALOR SERÃO ENTREGUES.
    OBS. CONSIDERE QUE O CAIXA POSSUI CEDULAS DE 50, 20, 10 E 1"""

not_50, not_20, not_10, not_1, saq = 0, 0, 0, 0, 0
saq = int(input('Qual valor você deseja sacar? R$ '))
vl = saq
while vl - 50 > 0:
    not_50 += 1
    vl -= 50
while vl - 20 > 0:
    not_20 += 1
    vl -= 20
while vl - 10 > 0:
    not_10 += 1
    vl -= 10
while vl - 1 > 0:
    not_1 += 1
    vl -= 1
print(f'''Valor do saque R$ {saq}
      {not_50} Notas de R$ 50,00
      {not_20} Notas de R$ 20,00
      {not_10} Notas de R$ 10,00
      {not_1} Notas de R$ 1,00''')
