# CRIE UM PROGRAMA QUE O USUARIO POSSA DIGITAR VARIOS VALORES NUMERICOS E CADASTRE-OS EM UMA
# LISTA, CASO O NUMERO JA ESTEJA NA LISTA, ELE NÃO SERÁ ADICIONADO. NO FINAL, SERÃO EXIBIDOS
# TODOS OS VALORES UNICOS DIGITADOS EM ORDEM CRESCENTE.

lista = list()
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
        print(f'O número {num} foi adicionado com sucesso')
    else:
        print(f'Já havia o número {num} na lista')
    resp = input(str(f'Deseja continuar? [S/N] '))
    if resp not in 'sSnN':
        resp = input(str('Resposta inválida, Deseja continuar? [S/N]'))
    elif resp in 'nN':
        break
print(lista)
print('Programa encerrado.')
