"""DESAFIO 020
O PROFESSOR AGORA QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHO DOS ALUNOS, FAÇA UM PROGRAMA QUE
LEIA O NOME DOS ALUNOS E MOSTRE A ORDEM SELECIONADA"""

from random import shuffle

a1 = str(input('Nome do Aluno 1: '))
a2 = str(input('Nome do Aluno 2: '))
a3 = str(input('Nome do Aluno 3: '))
a4 = str(input('Nome do Aluno 4: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A sequencia de apresentação é {}'.format(lista))
