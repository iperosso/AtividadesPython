""" CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM 'SILVA' NO NOME."""

nome = str(input('Digite o seu nome completo: ')).strip()
print('Seu nome tem Santos? {}'.format('santos' in nome.lower()))
