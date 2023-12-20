# CRIE UM PROGRAMA QUE TENHA UMA TUPLA COM VARIAS PALAVRAS, DEPOIS DISSO ELE DEVE MOSTRAR PARA CADA PALAVRA,
# QUAIS SÃO AS SUAS VOGAIS
palavras = ('caderno', 'lapis', 'apontador', 'caneta', 'borracha', 'estojo', 'tesoura')
for palavra in range(0, len(palavras)):
    print(f'Na palavra {palavras[palavra]} temos as vogais:', end=' ')
    for letra in palavras[palavra]:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
    print(end='\n')
