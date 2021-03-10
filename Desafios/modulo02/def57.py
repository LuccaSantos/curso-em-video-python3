'''
    Crie um script q leia o sexo de uma pessoa, mas só aceite valores 'm' ou 'f'
    caso receba outra resposta peça de novo ate uma resposta valida.
'''

print('= ' * 6 + '' + ' =' * 6)

contador = 0
while contador != 1:
    sexo = input('Informe seu sexo: \n[M] - MASCULINO\n[F] - FEMININO\n').upper()
    if (sexo == 'M') or (sexo == 'F'):
        contador = 1
    print('Informe um sexo valido')

print('FIM')

print('= ' * 15)