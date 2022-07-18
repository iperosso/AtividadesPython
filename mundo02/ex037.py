""" ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUARIO ESCOLHER
    QUAL SERÁ A BASE DA CONVERSÃO:
    > 1 PARA BINARIO
    > 2 PARA OCTAL
    > 3 PARA HEXADECIMAL """

num = int(input('Digite um número para fazer a Conversão'))
print('''Selecione a base da conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')
opc = int(input('Escolha a base'))
if opc == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opc == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opc == 3:
    print('{} convertido para HEXAGONAL é igua a {}'.format(num, hex(num)[2:]))
else:
    print('Escolha errada!')
