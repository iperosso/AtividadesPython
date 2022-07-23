""" MELHORE O JOGO DO DESAFIO 028 ONDE O COMPUTADOR VAI 'PENSAR' EM UM NÚMERO ENTRE 0 E 10
    SÓ QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATÉ ACERTAR, MOSTRANDO NO FINAL QUANTOS 
    PALPITES FORAM NECESSÁRIOS PARA VENCER"""
    
from random import randrange

print('=+=' * 29)
print('Vamos brincar de adivinhação? eu vou pensar em um número de 1 a 10 e você tenta advinhar')
print('=+=' * 29)
palpite_pc = randrange(1, 11)
player_palpite = 0
count = 0
while player_palpite != palpite_pc:
    player_palpite = int(input('Digite o seu palpite de 1 a 10: '))
    if count > 0:
        print(f'Você ja tentou {count}x sem sucesso')
    count += 1
print(f'Você acertou!! O meu número era {palpite_pc}, E você precisou de {count} tentativas para acertar')