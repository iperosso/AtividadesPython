""" DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS E MOSTRE A SOMA APENAS
    DAQUELES QUE FOREM PARES. SE O VALOR DIGITADO FOR IMPAR, DESCONSIDERE-O"""

soma = 0
count = 0
for n in range(1, 7):
    v = int(input(f'Digite o {n} valor inteiro'))
    if v % 2 == 0:
        soma += v
        count += 1
print(f'A soma dos {count} valores PAR, é de {soma}')
