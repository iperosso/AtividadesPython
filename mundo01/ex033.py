# FAÇA UM PROGRAMA QUE LEIA TRES NÚMEROS E MOSTRE QUAL O MAIOR E QUAL É O MENOR
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite o terceiro número: '))
menor, maior = n1, n1
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3
print('O menor númeor é {}, e o maior número é {}'.format(menor, maior))
