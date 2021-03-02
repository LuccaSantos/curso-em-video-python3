'''
    Crie um script que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo
    retangulo e calcule o comprimento da hipotenusa
'''
from math import pow, sqrt

print('= '*6 + 'HIPOTENUSA DO TRIANGULO RETANGULO DO CRLH' + ' ='*6)
cateto_oposto = float(input('Informe o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Informe o comprimento do cateto adjacente: '))
print('O valor da hipotenusa desse triangulo é {}'.format(sqrt(pow(cateto_oposto, 2)+pow(cateto_adjacente, 2))))

print('= '*15)
