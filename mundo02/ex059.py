# CRIE UM PROGRAMA QUE LEIA VARIOS VALORES E MOSTRE UM MENU NA TELA:
# > [1] SOMAR
# > [2] MULTIPLICAR
# > [3] MAIOR
# > [4] NOVOS NUMEROS
# > [5] SAIR DO PROGRAMA
# SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO.
opç = 0
num01 = float(input('Digite um valor: '))
num01 = float(input('Digite outro valor: '))
while opç != 5:
    print('''Que operação desejada
          [1] Para Somar
          [2] Para Multiplicar
          [3] Para identificar o maior
          [4] Novos números
          [5] Sair do programa''')
    opç = int(input('Digite a Operação que deseja fazer: '))
    if opç == 1:
        print(f'A soma entre {num01} e {num02} é {num01 + num02}')
    elif opç == 2:
        print(f'A multiplicação entre {num01} e {num02} é {num01 * num02}')
    elif opç == 3:
        if num01 > num02:
            print(f'Entre {num01} e {num02} o maior valor é {num01}')
        elif num01 < num02:
            print(f'Entre {num01} e {num02} o maior valor é {num02}')
        else:
            print(f'Entre {num01} e {num02} não tem maior, os dois são iguais')
    elif opç == 4:
        print('Digite então os novos valores por favor')
        num01 = float(input('Divite um valor: '))
        num02 = float(input('Digite outro valor: '))
    elif opç == 5:
        print('Encerrando a aplicação, obrigado!')
    else:
        print('Opção inválida, por favor, digite novamente')
        