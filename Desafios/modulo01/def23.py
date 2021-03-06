'''
    Crie um scritp que leia um numero de 0 a 9999 e mostre a decomposição do mesmo
'''

print('= '*6 + 'DECOMPOSIÇÃO DE NUMEROS' + ' ='*6)

numero = input('Informe um número de 0 a 9999: ')
unidades = numero[:1]
dezenas = numero[1:2]
centenas = numero[2:3]
unidade_milhar = numero[3:4]
print('Unidade: {}\nDezenas: {}\nCentenas: {}\nUnidade de milhar: {}'.format(unidades, dezenas, centenas, unidade_milhar))

print('= '*15)