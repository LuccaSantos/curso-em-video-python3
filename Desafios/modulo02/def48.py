'''
    Crie um script que calcule a soma de números impares q sao multiplos de tres e q se encontram no intervalo de 1 a 500
'''
import emoji
import time

print('= ' * 6 + 'SOMA DOS ÍMPARES MULTIPLOS DE TRES (1 A 500)' + ' =' * 6)

soma_primos_multiplos_de_3 = 0
for contador in range(1, 501):
    if (contador % 2 != 0):
        if (contador % 3 == 0):
            soma_primos_multiplos_de_3 += contador
            
print('A soma é igual a: {}'.format(soma_primos_multiplos_de_3))
print('= ' * 15)