""" FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE EM SEGUIDA O PRIMEIRO
    E O ULTIMO NOME SEPARADAMENTE. """

nome = str(input('Digite seu nome completo')).strip()
div = nome.split()
print('Seu primeiro nome é: {}'.format(div[0]))
print('Seu ultimo nome é: {}'.format(div[-1]))
