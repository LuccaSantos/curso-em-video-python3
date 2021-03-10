'''
    Crie um script que calcule o fatorial de um número 
'''

print('= ' * 6 + 'CALCULO DE FATORIAL!' + ' =' * 6)

numero = float(input('Informe o número: '))
contador = 1
fatorial = 1
while contador != numero:
    fatorial *= (numero)
    numero -= 1

print('O fatorial é {}'.format(fatorial))



print('= ' * 15)