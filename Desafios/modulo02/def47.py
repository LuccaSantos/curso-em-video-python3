'''
    Crie um script que mostre todos os números pares que estao no intervalo de 1 e 50
'''
import emoji
import time

print('= ' * 6 + 'PARES DE 1 A 50' + ' =' * 6)

for contador in range(1, 51):
    if (contador % 2 == 0):
        print(contador) 

print('= ' * 15)