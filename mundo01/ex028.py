# ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR PENSAR EM UM NUMERO INTEIRO ENTRE 0 E 5 E
# PEÇA PARA O USUARIO TENTAR DESCOBRIR QUAL FOI O NUMERO ESCOLHIDO PELO COMPUTADOR.
# O COMPUTADOR DEVE ESCREVER NA TELA SE O USUARIO VENCEU OU PERDEU.
from time import sleep
from random import randint
num = randint(0, 5)
print('=+=' * 25)
print('Vou pensar em um número de 0 a 5, será que você consegue adivinhar qual é?')
print('=+=' * 25)
sleep(3)
palp = int(input('Qual o seu palpite? '))
print('Processando...')
sleep(3)
if palp == num:
    print('Parabéns, você acertou!!!')
else:
    print('Que pena, você errou')
