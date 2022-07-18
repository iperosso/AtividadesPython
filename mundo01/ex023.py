""" FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE NA TELA CADA UMA TELA CADA
    UM DOS DIGITOS SEPARADOS."""

num = int(input('Digite um número entre 0 e 9999'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("""Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}""".format(u, d, c, m))
