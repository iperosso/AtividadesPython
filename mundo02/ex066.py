# DESNVOLVA UM PROGRAMA QUE LEIA VARIOS NÚMEROS INTEIROS PELO TECLADO.
# O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999, QUE É A CONDIÇÃO DE PARADA.
# NO FINAL, MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES
cont, soma = 0, 0
while True:
    num = int(input('Digite um valor inteiro [999 para encerrar]'))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Você digitou {cont} números, e a soma deles é de {soma}')
