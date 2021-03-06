'''
    Crie um script que le quatro nomes e sorteia um dos nomes
'''
import random

print('= '*6 + 'SORTEIO DE NOME' + ' ='*6)

nome1 = input('Informe um nome: ')
nome2 = input('Informe um nome: ')
nome3 = input('Informe um nome: ')
nome4 = input('Informe um nome: ')
print('O nome escolhido é {}'.format(random.choice([nome1, nome2, nome3, nome4])))

print('= '*15)