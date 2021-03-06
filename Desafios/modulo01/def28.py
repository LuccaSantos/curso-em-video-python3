'''
    Crie um script que escolha um número entre 0 e 5 para o usuario tentar descobrir
    o programa deve informar se o usuario venceu ou perdeu
'''

import random

print('= ' * 6 + 'SILVA OU NAO' + ' =' * 6)

numero = random.randrange(0, 5)
chute = int(input('Chuta um número de 0 a 5: '))
if chute == numero:
    print('Vc acertou, bruxão')
else:
    print('Erouuu! era {}!'.format(numero))

print('= ' * 15)
