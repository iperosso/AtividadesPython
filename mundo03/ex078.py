# FAÇA UM PROGRAMA QUE LEIA 5 VALORES NUMÉRICOS E GUARDE OS EM UMA LISTA.
# NO FINAL MOSTRE QUAL FOI O MAIOR E MENOR VALOR DIGITADO E AS SUAS RESPECTIVAS POSIÇÕES NA LISTA
lista = list()
menor = maior = cont = 0
while True:
    lista.append(int(input(f'Digite um valor inteiro para a posição {cont}: ')))
    if cont == 0:
        menor = lista[-1]
        maior = lista[-1]
    elif lista[-1] < menor:
        menor = lista[-1]
    elif maior < lista[-1]:
        maior = lista[-1]
    cont += 1
    if cont == 5:
        break
print('-.' * 10)
print(f'Os valores digitados foram: {lista}')
for c, v in enumerate(lista):
    if maior == v:
        print(f'O maior valor digitado foi {v} na posição {c}')
    elif menor == v:
        print(f'O menor valor digitado foi {v} na posição {c}')
print('-.' * 10)
