""" ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO N INTEIRO QUALQUER E MOSTRE NA TELA OS N 
    PRIMEIROS ELEMENTOS DE UMA SEQUENCIA DE FIBONACCI"""

qtd = int(input('Digite quantos termos da sequencia de Fibonacci você quer mostrar: '))
ant = 0
atu = 1
prox = 0
while qtd - 1 > 1:
    if ant == 0:
        print(ant, atu, end=' ')
    prox = atu + ant
    ant = atu
    atu = prox
    qtd -= 1
    print(prox, end=' ')
