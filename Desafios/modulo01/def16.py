'''
    Crie um script que leia um número real qualquer pelo teclado e mostre na tela sua parte inteira
'''

from math import trunc
print('= '*6 + 'PARTE INTEIRA' + ' ='*6)

numero = float(input('Informe um número real: '))
print('A parte inteira do número {} é {}'.format(numero, trunc(numero)))

print('= '*15)