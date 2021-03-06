'''
    Crie um script q leia um numero inteiro e diga se ele é ou nao primo
'''
import emoji

print('= ' * 6 + 'PRIMO OU NÃO' + ' =' * 6)

numero = int(input('Diga um número: '))
primo = False

for contador in range(1, numero + 1):
    if (numero % contador != 0):
        if (contador == numero) or (contador == 1):
            primo = True

if (primo == True):
    print('\U0001F92D É PRIMO')
else:
    print('\U0001F600 NÃO É PRIMO')

print('= ' * 15)
