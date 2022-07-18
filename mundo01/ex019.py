""" UM PROFESSOR QUER SORTEAR UM DOS SEUS 4 ALUNOS PARA APAGAR O QUADRO. FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO
    O NOME DELES E ESCREVENDO O NOME DO ESCOLHIDO."""

from random import choice

a1 = input('Nome do Aluno 1: ')
a2 = input('Nome do Aluno 2: ')
a3 = input('Nome do aluno 3: ')
a4 = input('Nome do aluno 4: ')
lista = [a1, a2, a3, a4]
sorteado = choice(lista)
print('O Aluno sorteado é {}'.format(sorteado))
