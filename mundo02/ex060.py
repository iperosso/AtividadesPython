""" FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER E MOSTRE O SEU FATORIAL"""

#from math import factorial
#num = int(input('Digite um número para calcular o seu fatorial: '))
#print(factorial(num))

#num = int(input('Digite um valor para calcular o seu fatorial: '))
#count = num - 1
#tot = 0
#while count > 0:
#    if tot == 0:
#        tot = num
#    tot = tot * count
#    count = count - 1
#print(tot)

num = int(input('Digite um número para calcular o seu fatorial: '))
tot = num
for n in range(num -1, 1, -1):
    tot = tot * n
print(tot)