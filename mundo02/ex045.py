# CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPO COM VOCÊ
from time import sleep
from random import randint
print('=+=' * 10)
print('    Vamos jogar Jokenpô?')
print('=+=' * 10)
sleep(1)
print('''Selecione o número que deseja:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
alt = int(input('Escolha seu palpite'))
pcalt = randint(1, 3)
print('Jo')
sleep(1)
print('ken')
sleep(1)
print('pô')
sleep(1)
if pcalt == 1:
    pcalt = 'Pedra'
elif pcalt == 2:
    pcalt = 'Papel'
else:
    pcalt = 'Tesoura'
if alt == 1:
    alt = 'Pedra'
elif alt == 2:
    alt = 'Papel'
else:
    alt = 'Tesoura'
if pcalt != alt:
    if pcalt == 'Pedra' and alt == 'Papel' or pcalt == 'Papel' and alt == 'Tesoura' or pcalt == 'Tesoura' and alt == 'Pedra':
        print('Você ganhou, você escolheu {} e eu escolhi {}'.format(alt, pcalt))
    else:
        print('Eu ganhei, você escolheu {} e eu escolhi {}'.format(alt, pcalt))
else:
    print('Empate, nós dois escolhemos {}'.format(alt))
