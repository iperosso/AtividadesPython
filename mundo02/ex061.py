# REFAÇA O DESAFIO 051, LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PA, MOSTRANDO OS
# 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO A ESTRUTURA WHILE
ter = int(input('Digite o termo da P.A.: '))
raz = int(input('Digite a razão da P.A.: '))
tot = ter
count = 1
while count < 11:
    tot += raz
    print(f'{tot}', end=' ')
    count += 1
