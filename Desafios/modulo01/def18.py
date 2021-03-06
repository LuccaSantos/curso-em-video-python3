'''
    Crie um script que leia um angulo qualquer e mostre na tela o valor 
    do seno cosseno e tangente desse angulo
'''
from math import radians, sin, cos, tan
print('= '*6 + 'SENO COSSENO E TANGENTE' + ' ='*6)

angulo = radians(float(input('Informe o valor do angulo: ')))

seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)

print('Para o angulo de {} temos:\nseno: {:.2}\ncosseno: {:.2}\ntangente: {:.2}'.format(angulo, seno, cosseno, tangente))

print('= '*15)