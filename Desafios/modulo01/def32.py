'''
    Crie um script que leia um ano qualquer e mostre se ele é bissexto
'''
print('= ' * 6 + 'ANO BISSEXTO' + ' =' * 6)

ano = int(input('Informe um ano: '))
if (ano % 4 == 0):
    if (ano / 100 != 0):
        print('É bissexto!')
    else:
        print('Não é bissexto!')
else:
    if (ano / 400 != 0):
        print('Não é bissexto!')
    else:
        print('É bissexto!')

print('= ' * 15)