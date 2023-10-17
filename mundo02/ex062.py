# MELHORE O DESAFIO 061, PERGUNTANDO PARA O USUARIO SE ELE QUER MOSTRAR MAIS ALGUNS TERMOS
# O PROGRAMA ENCERRA QUANDO ELE MOSTRAR 0 TERMOS
ter = int(input('Digite o termo para iniciar a P.A.: '))
raz = int(input('Digite a razão para essa P.A.:'))
tot = ter
count = 10
while count > 1:
    tot += raz
    print(f'{tot}', end=' ')
    count -= 1
    if count == 1:
        count = int(input('\nQuer mostrar mais quantos termos? '))
