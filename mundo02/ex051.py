""" DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA, NO FINAL
    MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO"""

termo = int(input('A progressão deve iniciar de qual termo?'))
razao = int(input('Qual a razão dessa progressão?'))
count = 1
for i in range(termo, (termo + razao * 10), razao):
    print(f'O {count} termo dessa razão é {i}')
    count += 1
