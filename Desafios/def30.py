'''
    Crie um script que leia um número e diga se é par ou impar
'''
print('= ' * 6 + 'PAR OU ÍMPAR' + ' =' * 6)

numero = int(input('Informe um número inteiro: '))
if (numero % 2) == 0:
    print('PAR')
else:
    print('ÍMPAR')
print('= ' * 15)
