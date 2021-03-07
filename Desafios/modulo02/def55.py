'''
    Crie um script q leia o peso de 5 pessoas e informe qual o mais gordo e o mais palito
'''

print('= ' * 6 + 'GORDO E MAGRO' + ' =' * 6)

mais_gordo = 0
mais_palito = 0
for contador in range(1, 6):
    peso = float(input('Informe o peso: '))
    if contador == 1:
        mais_palito = peso
        mais_gordo = peso
    else: 
        if peso > mais_gordo:
            mais_gordo = peso
        if peso < mais_palito:
            mais_palito = peso
print('O mais bolota pesa: {} e o mais chassi de grilo: {}'.format(
    mais_gordo, mais_palito))

print('= ' * 15)