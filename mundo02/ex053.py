# CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM PALINDROMO,
# DESCONSIDERE OS ESPAÇO
frase = str(input('Digite uma frase para analisar: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'A frase {junto} lida ao contrário fica {inverso}')
if junto == inverso:
    print('Isso é um palindromo')
else:
    print('Isso não é um palindromo')
