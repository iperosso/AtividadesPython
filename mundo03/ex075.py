""" DESENVOLVA UM PROGRAMA QUE LEIA QUATRO VALORES PELO TECLADO E GUARDE-OS EM UMA TUPLA
    E NO FINAL MOSTRE
    > QUANTAS VEZES APARECEU O VALOR 9
    > EM POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR = 3
    > QUAIS FORAM OS NÚMEROS PARES"""

num1 = int(input('Digite um valor inteiro: '))
num2 = int(input('Digite um valor inteiro: '))
num3 = int(input('Digite um valor inteiro: '))
num4 = int(input('Digite um valor inteiro: '))
lista = (num1, num2, num3, num4)
par = ()
print(f'Os números digitados foram {lista}')
if 9 in lista:
    print(f'O 9 aparece {lista.count(9)} vezes')
if 3 in lista:
    print(f'O 3 aparece primeiro na posição {lista.index(3) + 1}')
for n in len(lista):
    if n % 2 == 0:
        n.append(par)
print(par)