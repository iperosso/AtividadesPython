# DESENVOLVA UM PROGRAMA QUE LEIA, O NOME, IDADE E SEXO DE 4 PESSOAS
# E NO FINAL MOSTRE A MÉDIA DE IDADE DO GRUPO, QUAL É O NOME DO HOMEM MAIS VELHO
# E QUANTAS MULHERES TEM MENOS DE 20 ANOS
media_idade = 0
homem_mais_velho = ''
idade_mais_alta = 0
mulher_menor_idade = 0
qtd_pessoas = 4
for p in range(1, qtd_pessoas + 1):
    nome = str(input(f'Digite o nome da {p} pessoa: ')).strip().capitalize()
    idade = int(input(f'Digite a idade de {nome}: '))
    sexo = str(input(f'Qual o sexo de {p} (Digite M ou F): ')).strip().upper()
    media_idade += idade
    if idade_mais_alta == 0:
        idade_mais_alta = idade
    if sexo == 'M' and idade > idade_mais_alta:
        idade_mais_alta = idade
        homem_mais_velho = nome
    elif sexo == 'F' and idade < 18:
        mulher_menor_idade += 1
print(f'A média de idade do grupo é {media_idade / qtd_pessoas}')
print(f'O homem mais velho é {homem_mais_velho} com {idade_mais_alta} anos')
print(f'O grupo tem {mulher_menor_idade} mulheres com menos de 18 anos')
