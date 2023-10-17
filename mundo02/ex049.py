# REFAÇA O DESAFIO 009, MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUÁRIO ESCOLHER,
# SÓ QUE AGORA UTILIZANDO O LAÇO FOR
num = int(input('Qual tabuada você quer consultar?'))
for n in range(11):
    print(f'{num} x {n} = {num * n}')
    