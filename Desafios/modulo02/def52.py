'''
    Crie um script q leia um numero inteiro e diga se ele é ou nao primo
'''
import emoji

print('= ' * 6 + 'PRIMO OU NÃO' + ' =' * 6)

numero = int(input('Diga um número: '))
numero_de_divisores = 0

for contador in range(1, numero + 1):
    if (numero % contador == 0):
        numero_de_divisores += 1

if (numero_de_divisores == 2):
    print('\U0001F92D É PRIMO')
else:
    print('\U0001F600 NÃO É PRIMO')

print('= ' * 15)
