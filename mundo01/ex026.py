# FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE
# > QUANTAS VEZES APARECE A LETRA 'A'
# > EM QUE POSIÇÃO ELA APARECE PELA PRIMEIRA VEZ
# > EM QUE POSIÇÃO ELA APARECE PELA ULTIMA VEZ
frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes'.format(frase.lower().count('a')))
print('A letra A aparece pela primeira vez na posição {}'.format(frase.lower().find('a') + 1))
print('A letra A aparece pela útima vez na posição {}'.format(frase.lower().rfind('a') + 1))
