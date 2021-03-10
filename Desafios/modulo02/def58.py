'''
    Melhore o jogo  do desafio 28 onde o computador vai 'pensar' em um numero de 0 a 10
    onde o jogador vai chutando valores e quando acertar mostre a quantidade de chutes
'''
from math import e
import random

print('= ' * 6 + '' + ' =' * 6)

numero_chutes = 0
tentativa = True
numero = random.randrange(0, 11)
while tentativa:
    chute = int(input('Chute um número de 0 a 10: '))
    if numero == chute:
        print('ACERTOU!!!')
        tentativa = False
    else:
        numero_chutes += 1
        print('ERROU')

print('= ' * 15)