# CRIE UM PROGRAMA QUE TENHA UMA TUPLA UNICA COM NOMES DE PRODUTOS E SEUS RESPECTIVOS PREÇOS NA SEQUENCIA.
# NO FINAL, MOSTRE UMA LISTAGEM DE PREÇOS, ORGANIZANDO OS DADOS EM FORMA TABULAR
listagem = ('Macarrão', 3.25, 'Molho Tomate', 4.89, 'Calabresa', 6.99, 'Queijo Ralado', 4.99)
print('-' * 30)
print('Listagem de preços'.center(30))
print('-' * 30)
for i in range(0, len(listagem), 2):
    print(f'{listagem[i].ljust(22, ".")} R$ {listagem[i + 1]:>.2f}')
print('-' * 30)
