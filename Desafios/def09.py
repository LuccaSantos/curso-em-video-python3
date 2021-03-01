'''
    Crie um script que leia um número inteiro 
    e mostre na tela sua tabuada
'''

print('= '*6 + 'TABUADA' + ' ='*6)
numero  = int(input('Informe o número da tabuada: '))

print('  {} x 0 = {:^5}'.format(numero, numero*0))
print('  {} x 1 = {:^5}'.format(numero, numero*1))
print('  {} x 2 = {:^5}'.format(numero, numero*2))
print('  {} x 3 = {:^5}'.format(numero, numero*3))
print('  {} x 4 = {:^5}'.format(numero, numero*4))
print('  {} x 5 = {:^5}'.format(numero, numero*5))
print('  {} x 6 = {:^5}'.format(numero, numero*6))
print('  {} x 7 = {:^5}'.format(numero, numero*7))
print('  {} x 8 = {:^5}'.format(numero, numero*8))
print('  {} x 9 = {:^5}'.format(numero, numero*9))
print('  {} x 10 = {}'.format(numero, numero*10))

print('= '*15)
