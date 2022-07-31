""" FAÇA UM PROGRAMA QUE JOGUE PAR OU IMPAR COM O COMPUTADOR. O JOGO SERÁ INTERROMPIDO
    QUANDO O JOGADOR PERDER, MOSTRANDO O TOTAL DE VITÓRIAS CONSECUTIVAS ELE CONQUISTOU"""

from random import randint

print('=+=' * 7)
print('Jogo Par ou Ímpar')
print('=+=' * 7)
player_wins = 0
while True:
    esc_jog = ''
    while esc_jog not in 'pPiI':
        esc_jog = str(input('Par ou Ímpar? [P/I]')).upper().split()[0]
    palp_player = int(input('Digite um valor'))
    palp_pc = randint(1, 11)
    print('-' * 15)
    print(f'Você escolheu {palp_player} e o computador escolheu {palp_pc}, total {palp_pc + palp_player}')
    print('-' * 15)
    if palp_pc + palp_player % 2 == 0 and esc_jog == 'P':
        player_wins += 1
        print('Você venceu!')
        print('Vamos novamente...')
        print('=' * 15)
    elif palp_pc + palp_player % 2 != 0 and esc_jog == 'I':
        player_wins += 1
        print('Você venceu!')
        print('Vamos novamente...')
        print('=' * 15)
    else:
        break
print(f'Fim de jogo, você vendeu {player_wins} vezes')
