""" CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE 7 PESSOAS E NO FINAL MOSTRE QUANTAS
    PESSOAS AINDA NÃO ATINGIRAM A MAIOR IDADE E QUANTAS JÁ SÃO MAIORES."""

qtd_maior = 0
qtd_menor = 0
qtd_pessoas = 8
for p in range(1, qtd_pessoas):
    nome = str(input(f'Digite o nome da {p} pessoa: '))
    idade = int(input(f'Digite a idade de {nome}: '))
    if idade >= 18:
        qtd_maior += 1
    else:
        qtd_menor += 1
print(f'Temos {qtd_maior} pessoas MAIORES de idade e {qtd_menor} MENORES de idade')
