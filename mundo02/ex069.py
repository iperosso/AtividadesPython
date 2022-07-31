""" CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VARIAS PESSOAS. A CADA PESSOA CADASTRADA
    O PROGRAMA DEVERA PERGUNTAR SE O USUARIO QUER OU NÃO CONTINUAR. E NO FINAL MOSTRAR.
    > QUANTAS PESSOAS TEM MAIS DE 18 ANOS
    > QUANTOS HOMENS FORAM CADASTRADOS
    > QUANTAS MULHERES TEM MENOS DE 20 ANOS"""

total_h, m_menos_20, maior_idade, idade = 0, 0, 0, 0
while True:
    print('=x=' * 15)
    print('==x==x==x==x= Cadastro Pessoal =x==x==x==x==')
    print('=x=' * 15)
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Opção errada, digite o sexo corretamente [M/F] ')).upper().strip()[0]
    idade = int(input('Idade: '))
    if idade > 18:
        maior_idade += 1
    if sexo == 'M':
        total_h += 1
    if idade < 20 and sexo == 'F':
        m_menos_20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Opção inválida, por favor selecione a opção correta. Deseja continuar? [S/N]')).upper().strip()[0]
    if resp in 'N':
        break
print(f'Foram cadastradas {m_menos_20} mulheres com menos de 20 anos.')
print(f'Foram cadastrados {total_h} homens.')
print(f'Foram cadastrados {maior_idade} pessoas maiores de idade')
