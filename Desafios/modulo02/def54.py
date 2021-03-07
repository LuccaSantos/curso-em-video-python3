'''
    Crie um script q leia o ano de nascimento de sete pessoas e no final mostre quantas pessoas 
    sao maiores e menores de idade
'''

print('= ' * 6 + 'MAIORIADE' + ' =' * 6)

numero_de_maiores = 0
numero_de_menores = 0
for contador in range(1, 8):
    ano_nascimento = int(input('Informe o ano do seu nascimento: '))
    idade = 2021 - ano_nascimento
    if (idade >= 18):
        numero_de_maiores += 1
    else:
        numero_de_menores += 1
print('Esse grupo de pessoas possue: {} maiores e {} menores de idade'.format(
    numero_de_maiores, numero_de_menores))

print('= ' * 15)