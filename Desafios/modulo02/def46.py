'''
    Crie um script que mostre na tela uma contagem regressiva para o estouro de fogos de artificios, indo de 10
    até 0, indO 10 ate 0, com uma pausa de 1 segundo entre elas.
'''
import emoji
import time

print('= ' * 6 + 'FIREWORKS' + ' =' * 6)

for contador in range(10, -1, -1):
    if contador == 0:
        print(emoji.emojize(':fireworks:'))
    else:
        print(contador)
    contador =+ 1
    time.sleep(1)
print('= ' * 15)