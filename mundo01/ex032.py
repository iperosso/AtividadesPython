""" FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO"""

from calendar import isleap
from datetime import date

ano = int(input('Digite o ano que deseja consultar, para consultar o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year
if isleap(ano):
    print('O ano {} é Bissexto.'.format(ano))
else:
    print('O ano {} Não é Bissexto.'.format(ano))
