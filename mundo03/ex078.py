# FAÇA UM PROGRAMA QUE LEIA 5 VALORES NUMÉRICOS E GUARDE OS EM UMA LISTA.
# NO FINAL MOSTRE QUAL FOI O MAIOR E MENOR VALOR DIGITADO E AS SUAS RESPECTIVAS POSIÇÕES NA LISTA
lista = list()
menor = maior = 0
for i in range(0, 5):
    lista.append(int(input('Digite um valor inteiro:  ')))
    if menor == 0:
        menor = lista[-1]
        maior = lista[-1]
    elif lista[-1] < menor:
        menor = lista[-1]
    elif maior < lista[-1]:
        maior = lista[-1]
print('-.' * 10)
print(f'Os valores digitados foram: {lista}')
print('-.' * 10)
print(f'O maior valor digitado foi: {maior}')
print(f'O menor valor digitado foi: {menor}')
print('-.' * 10)
