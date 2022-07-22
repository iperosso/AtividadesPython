""" FAÇA UM PROGRAMA QUE LEIA O PESO DE CINCO PESSOAS E NO FINAL MOSTRE QUAL FOI
    O MAIOR E O MENOR PESO LIDOS"""

maior_peso = 0
menor_peso = 0
nome_maior_peso = ''
nome_menor_peso = ''
qtd_pessoas = 5
for p in range(1, qtd_pessoas + 1):
    nome = str(input(f'Digite o nome da {p} pessoa: '))
    peso = float(input(f'Digite o peso de {nome} em Kg: '))
    if maior_peso == 0 and menor_peso == 0:
        maior_peso = peso
        menor_peso = peso
        nome_maior_peso = nome
        nome_menor_peso = nome
    if peso < menor_peso:
        menor_peso = peso
        nome_menor_peso = nome
    elif peso > maior_peso:
        maior_peso = peso
        nome_maior_peso = nome
print(f'A pessoa com maior peso é {nome_maior_peso} com {maior_peso}Kg')
print(f'A pessoa com menor peos é {nome_menor_peso} com {menor_peso}Kg')
