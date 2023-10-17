# DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTANCIA DE UMA VIAGEM EM KM.
# CALCULE PREÇO DA PASSAGEM, COBRANDO R$ 0,50 POR KM PARA VIAGENS DE ATÉ 200KM
# E R$ 0,45 PARA VIAGENS MAIS LONGAS
dist = int(input('Qual a distância da viagem? '))
if dist < 200:
    tar = dist * 0.50
    print('O valor da tarifa é R$ {:.2f}'.format(tar))
else:
    tar = dist * 0.45
    print('O valor da tarifa é R$ {:.2f}'.format(tar))
