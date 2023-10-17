# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU NÃO UM NÚMERO PRIMO
num = int(input('Digite um número inteiro para analisar'))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
if count == 2:
    print(f'O número {num} É PRIMO')
else:
    print(f'O número {num} NÃO É PRIMO')
