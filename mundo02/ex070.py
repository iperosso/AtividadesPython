# CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VARIOS PRODUTOS. O PROGRAMA DEVERÁ PERGUNTAR
# SE O USUARIO VAI CONTINUAR, E NO FINAL MOSTRE:
# > QUAL O TOTAL GASTO
# > QUANTOS PRODUTOS CUSTAM MAIS QUE R$ 1000
# > QUAL O NOME DO PRODUTO MAIS BARATO
total, p_mais_1000, p_mais_barato = 0, 0, 0
nome_p_mais_barato = ''
while True:
    produto = str(input('Nome do produto: ')).capitalize().strip()
    valor = float(input('Preço: R$ '))
    total += valor
    if p_mais_barato == 0 or valor < p_mais_barato:
        p_mais_barato = valor
        nome_p_mais_barato = produto
    elif valor > 1000:
        p_mais_1000 += 1
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print('-----Fim-----')
print(f'O total da compra foi R${total:.2f}.')
print(f'Tem {p_mais_1000} produtos mais caros que R$ 1000,00')
print(f'O produto mais barato foi {nome_p_mais_barato} que custa R$ {p_mais_barato:.2f}.')