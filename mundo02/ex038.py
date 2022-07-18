""" ESCREVA UM PROGRAMA QUE LEIA DOIS NUMEROS INTEIROS E COMPARE-OS, MOSTRANDO NA TELA
    UMA MENSAGEM:
    > O PRIMEIRO VALOR É MAIOR
    > O SEGUNDO VALOR É MAIOR
    > NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS"""
a = int(input('Digite um valor inteiro: '))
b = int(input('Digite outro valor inteiro: '))
if a > b:
    print('O primeiro valor é maior.')
elif b > a:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais')
