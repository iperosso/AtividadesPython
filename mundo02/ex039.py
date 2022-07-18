""" FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM
    A SUA IDADE, SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR, SE É A HORA EXATA DE
    SE ALISTAR OU SE JÁ PASSOU DO TEMPO DO ALISTAMENTO. SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR
    O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO."""

from datetime import date

ano = int(input('Que ano você nasceu?'))
idade = date.today().year - ano
if idade == 18:
    print('Já está na hora de se alistar para o serviço militar')
elif idade > 18:
    dif = idade - 18
    print('Já se passaram {} anos do seu serviço militar'.format(dif))
else:
    dif = 18 - idade
    print('Ainda faltam {} anos para você poder se alistar'.format(dif))
