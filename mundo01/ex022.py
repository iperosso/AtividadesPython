# CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE
# 1* O NOME COM TODAS AS LETRAS MAIÚSCULAS
# 2* O NOME COM TODAS AS LETRAS MINÚSCULAS
# 3* QUANTAS LETRAS TEM NO TOTAL (SEM CONSIDERAR OS ESPAÇOS)
# 4* QUANTAS LETRAS TEM O PRIMEIRO NOME
nome = str(input('Qual o seu nome completo?'))
print(nome.upper())
print(nome.lower())
div = nome.count(' ')
print('Seu nome tem: ', len(nome) - div, 'letras')
print('Seu primeiro nome tem: ', nome.find(' '), 'letras')
