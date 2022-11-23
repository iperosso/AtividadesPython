""" DESENVOLVA UM PROGRAMA QUE LEIA QUATRO VALORES PELO TECLADO E GUARDE-OS EM UMA TUPLA
    E NO FINAL MOSTRE
    > QUANTAS VEZES APARECEU O VALOR 9
    > EM POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR = 3
    > QUAIS FORAM OS NÚMEROS PARES"""

lista = (int(input('Digite um valor inteiro: ')), int(input('Digite outro valor inteiro: ')), int(input('Digite mais um valor inteiro: ')), int(input('Digite o último valor inteiro: ')))
print(f'Os números digitados foram {lista}')
if 9 in lista:
    print(f'O 9 aparece {lista.count(9)} vezes')
else:
    print('O número 9 não aparece nenhuma vez.')
if 3 in lista:
    print(f'O 3 aparece primeiro na posição {lista.index(3) + 1}')
else:
    print('O número 3 não aparece nenhuma vez.')
cont = 0
for n in lista:
    if n % 2 == 0:
        if cont == 0:
            print('Os números pares são: ', end=' ')
        print(f'{n}', end=' ')
        cont += 1
