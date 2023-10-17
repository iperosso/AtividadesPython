# A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO
# DE UM ATLETA E MOSTRE A SUA CATEGORIA, DE ACORDO COM A IDADE:
# >ATÉ 9 ANOS: MIRIM
# >ATÉ 14 ANOS: INFANTIL
# >ATÉ 19 ANOS: JUNIOR
# >ATÉ 25 ANOS: SENIOR
# >ACIMA DE 25 ANOS: MASTER
from datetime import date
ano = int(input('Que ano o atleta nasceu? '))
idade = date.today().year - ano
if idade <= 9:
    print('Esse atleta é da categoria: MIRIM')
elif idade <= 14:
    print('Esse atleta é da categoria: INFANTIL')
elif idade <= 19:
    print('Esse atleta é da categoria: JUNIOR')
elif idade <= 25:
    print('Esse atleta é da categoria: SENIOR')
else:
    print('Esse atleta é da categoria: MASTER')
