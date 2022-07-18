""" DESAFIO 005
    FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E SEU ANTECESSOR."""

n = int(input('Digite um número'))
suc = n + 1
ant = n - 1
print('Você digitou o número {}, seu antecessor é {}, e o seu sucessor é {}'.format(n, ant, suc))
