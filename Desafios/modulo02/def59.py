'''
    Crie uma calculadora 
'''

print('= ' * 6 + '' + ' =' * 6)

contador = 's'
while contador != 'n':
    numero_um = float(input('Informe o primeiro número: '))
    numero_dois = float(input('Informe o segundo número: '))
    operador = int(input('Escolha o operador:\n[1] +\n[2] -\n[3] *\n[4] /\n'))
    if operador == 1:
        print('{} + {} = {}'.format(numero_um,  numero_dois, (numero_um + numero_dois) ))
        contador = input('DESEJA CONTINUAR? [s/n]? ').lower()
    elif operador == 2:
        print('{} - {} = {}'.format(numero_um,  numero_dois, (numero_um - numero_dois) ))
        contador = input('DESEJA CONTINUAR? [s/n]? ').lower()
    elif operador == 3:
        print('{} * {} = {}'.format(numero_um,  numero_dois, (numero_um * numero_dois) ))
        contador = input('DESEJA CONTINUAR? [s/n]? ').lower()
    elif operador == 4:
        print('{} / {} = {}'.format(numero_um,  numero_dois, (numero_um / numero_dois) ))
        contador = input('DESEJA CONTINUAR? [s/n]? ').lower()


print('= ' * 15)