""" FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU NÃO UM NÚMERO PRIMO"""

num = int(input('Digite o número que você deseja analisar: '))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end=' ')
        count += 1
    else:
        print('\033[31m', end=' ')
    print(f'{i}', end=' ')
print(f'\n\033[mO número {num} foi dividido {count}x')
if count <= 2:
    print('Por isso ele é um número PRIMO')
else:
    print('Por isso ele NÃO È UM NÚMERO PRIMO')
