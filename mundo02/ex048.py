""" FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS QUE SÃO MÚLTIPLOS DE 3
    E QUE SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500."""
soma = 0
count = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        count += 1
        soma += n
print(f'A soma de todos os {count} valores é de {soma}')
