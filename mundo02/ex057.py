""" FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE OS VALORES
    'M' OU 'F'. CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE ATÉ TER UM 
    VALOR CORRETO"""

vl = 0
while vl < 1:
    sexo = str(input('Qual o seu sexo? [M/F]')).upper()
    if sexo == 'F' or sexo == 'M':
        vl += 1
    else:
        print('Alternativa incorreta, por favor responda apenas com "F" ou "M"')
    if sexo == 'F':
        sexo = 'uma Benina'
    elif sexo == 'M':
        sexo = 'um Benino'
print(f'Você é {sexo}')
