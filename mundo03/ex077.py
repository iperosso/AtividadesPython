# CRIE UM PROGRAMA QUE TENHA UMA TUPLA COM VARIAS PALAVRAS, DEPOIS DISSO ELE DEVE MOSTRAR PARA CADA PALAVRA,
# QUAIS SÃO AS SUAS VOGAIS
palavras = ('caderno', 'lapis', 'apontador', 'caneta', 'borracha', 'estojo', 'tesoura')
for p in range(0, len(palavras)):
    print(f'Na palavra {palavras[p]} temos as vogais', end=' ')
    for l in palavras[p]:
        if l in 'aeiou':
            print(l, end=' ')
    print(end='\n')
