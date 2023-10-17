# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E MOSTRE NA TELA A SUA TABUADA.
num = int(input('Digite o número que você deseja saber a tabúada '))
x2, x3, x4, x5, x6, x7, x8, x9, x10 = num * 2, num * 3, num * 4, num * 5, num * 6, num * 7, num * 8, num * 9, num * 10
print(17 * 'x')
print('A tabúada de {} é.'.format(num))
print('{0} x  1 = {0:2}\n{0} x  2 = {1}\n{0} x  3 = {2}\n{0} x  4 = {3}\n{0} x  5 = {4}'.format(num, x2, x3, x4, x5,))
print('{0} x  6 = {1}\n{0} x  7 = {2}\n{0} x  8 = {3}\n{0} x  9 = {4}\n{0} x 10 = {5}'.format(num, x6, x7, x8, x9, x10))
print(17 * 'x')
