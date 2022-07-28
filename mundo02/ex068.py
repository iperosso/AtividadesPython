""" FAÇA UM PROGRAMA QUE JOGUE PAR OU IMPAR COM O COMPUTADOR. O JOGO SERÁ INTERROMPIDO
    QUANDO O JOGADOR PERDER, MOSTRANDO O TOTAL DE VITÓRIAS CONSECUTIVAS ELE CONQUISTOU"""

from random import randint

print('=+=' * 7)
print('Jogo Par ou Ímpar')
print('=+=' * 7)
esc_jog = ''
palp_pc = randint(1, 11)
palp_player = 0
while True:
    esc_jog = str(input('Par ou Ímpar? [P/I]')).upper().split()[0]
    if esc_jog == 'P':
        
