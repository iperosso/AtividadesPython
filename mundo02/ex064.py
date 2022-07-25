""" CRIE UM PROGRAMA QUE LEIA VARIOS NÚMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ VAI PARAR
    QUANDO O USUARIO DIGITAR 999, QUE É A CONDIÇÃO DE PARADA. NO FINAL MOSTRE QUANTOS NÚMEROS
    FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES (DESCONSIDERANDO O FLAG)"""

cont, soma, valor = 0, 0, 0
while valor != 999:
    valor = int(input('Digite um valor inteiro: '))
    if valor != 999:
        soma += valor
        cont += 1
print(f'Você digitou {cont} valores e a soma deles é de {soma}')
