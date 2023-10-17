# DESENVOLVA UMA LOGICA QUE LEIA O PESO E ALTURA DE UMA PESSOA, CALCULE SEU INDICE
# DE MASSA CORPORAL (IMC) E MOSTRE SEU STATUS, DE ACORDO COM A TABELA ABAIXO:
# >IMC ABAIXO DE 18,5: ABAIXO DO PESO
# >ENTRE 18,5 E 25: PESO IDEAL
# >25 ATÉ 30: SOBREPESO
# >30 ATÉ 40: OBESIDADE
# ACIMA DOS 40: OBESIDADE MORBIDA
peso = float(input('Qual a seu peso? KG '))
altura = float(input('Qual a sua altura em metros? '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Você tem um IMC de {:.1f}, que representa que você está abaixo do peso'.format(imc))
elif imc < 25:
    print('Você tem um IMC de {:.1f}, que representa que você está no peso ideal'.format(imc))
elif imc < 30:
    print('Você tem um IMC de {:.1f}, que representa que você está com sobrepeso'.format(imc))
elif imc < 40:
    print('Você tem um IMC de {:.1f}, que representa que você está com obesidade'.format(imc))
else:
    print('Você tem um IMC de {:.1f}, que representa que você está com obesidade morbida'.format(imc))
