"""DESAFIO 010
CRIE UM PROGRAMA QUE LEIA UMA QUANTIA DE DINHEIRO EM REAIS E CONVERTA EM DÓLARES"""

vr = float(input('Digite o valor em Reais para converter para Dólar'))
vd = float(input('Digite a cotação atual do Dólar'))
vc = vr / vd
print('A quantia digitada foi de R${}, com isso você compra {:.2}USD'.format(vr, vc))
