'''
    Crie um script que le quatro nomes de alunos e mostre os quatro em uma ordem sorteada para apresentação
'''

import random

print('= '*6 + 'EMBARALHAR NOMES' + ' ='*6)

nome1 = input('Informe um nome: ')
nome2 = input('Informe um nome: ')
nome3 = input('Informe um nome: ')
nome4 = input('Informe um nome: ')
print('A ordem escolhida é {}'.format(random.sample([nome1, nome2, nome3, nome4], k=4)))

print('= '*15)