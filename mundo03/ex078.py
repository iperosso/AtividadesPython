""" FAÇA UM PROGRAMA QUE LEIA 5 VALORES NUMÉRICOS E GUARDE OS EM UMA LISTA.
    NO FINAL MOSTRE QUAL FOI O MAIOR E MENOR VALOR DIGITADO E AS SUAS RESPECTIVAS POSIÇÕES NA LISTA"""

lista = list()
menor = maior = 0
for i in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
print(f'Os valores digitados foram: {lista}')
if menor == 0:
    menor = lista[1]
    maior = lista[1]
for c, v in enumerate(lista):
    if v < menor: