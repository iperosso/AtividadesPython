# FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE ANGULO.
from math import cos, sin, tan, radians
num = float(input('Digite o ângulo'))
seno = sin(radians(num))
coss = cos(radians(num))
tang = tan(radians(num))
print('O ângulo {:.2f}º tem o seno de {:.2f}'.format(num, seno))
print('O ângulo {:.2f}º tem o cossenho de {:.2f}'.format(num, coss))
print('O ângulo {:.2f}º tem o tangente de {:.2f}'.format(num, tang))
