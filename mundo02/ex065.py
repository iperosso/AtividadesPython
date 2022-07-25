""" CRIE UM PROGRAMA QUE LEIA VARIOS NÚMEROS INTEIROS PELO TECLADO. NO FINAL DA EXECUÇÃO
    MOSTRE A MEDIA DE TODOS OS VALORES E QUAL FOI O MAIOR E MENOR VALORES LIDOS. O PROGRAMA
    DEVE PERGUNTAR AO USUARIO SE ELE QUER OU NÃO CONTINUAR A DIGITAR VALORES"""

resp = 'S'
media, maior, menor, cont = 0, 0, 0, 0
while resp == 'S':
    num = int(input('Digite um valor inteiro'))
    if media == 0:
        menor = num
        maior = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    media += num
    cont += 1
    resp = str(input('Quer continuar adicionando números? [S/N] ')).upper().strip()
print(f'O maior número foi {maior}, o menor número foi {menor} e a média dos números foi {media/cont}')
