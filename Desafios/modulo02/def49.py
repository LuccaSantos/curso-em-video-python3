'''
    Refaca o def09 mostrando a tabuada de um número q o usuario escolheu com um laco for
'''

print('= ' * 6 + 'TABUADA COM FOR' + ' =' * 6)

numero = int(input('Informe um número: '))
for contador in range(1, 11):
    print('{} * {} = {}'.format(contador, numero, numero*contador))

print('= ' * 15)