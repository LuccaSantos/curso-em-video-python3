'''
    Crie um script que leia um número real qualquer pelo teclado e mostre na tela sua parte inteira
'''

print('= '*6 + 'PARTE INTEIRA' + ' ='*6)

from math import trunc
numero = float(input('Informe um número real: '))
print('A parte inteira do número {} é {}'.format(numero, trunc(numero)))

print('= '*15)