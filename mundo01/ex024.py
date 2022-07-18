""" CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO COM O NOME
    'SANTO'."""

cid = str(input('Digite o nome da cidade: ')).strip()
print(cid[:5].lower() == 'santo')
