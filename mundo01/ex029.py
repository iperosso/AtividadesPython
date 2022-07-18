""" ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO. SE ELE ULTRAPASSAR 80KM/H,
    MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
    A MULTA VAI CUSTAR R$ 7,00 POR CADA KM A CIMA DO LIMITE"""

from time import sleep

vel = int(input('Qual a velocidade do veiculo? Km/h'))
print('Processando...')
sleep(3)
if vel <= 80:
    print('Continue dirigindo com segurança.')
else:
    multa = (vel - 80) * 7
    print('Você está acima do limite de velocidade de 80Km/h e foi multado no valor de R$ {}'.format(multa))
