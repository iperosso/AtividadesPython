""" FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU TIPO PRIMITIVO E TODAS AS INFORMAÇÕES
    POSSIVEIS SOBRE ELE"""

obj = input('Digite algo')
print(type(obj))
print('É alfanumerico?', obj.isalnum())
print('É alfabético?', obj.isalpha())
print('É numérico?', obj.isnumeric())
print('Está escrito em minúsculo?', obj.islower())
print('Está escrito em maiúsculo?', obj.isupper())
print('Os caracteres podem ser impresso?', obj.isprintable())
