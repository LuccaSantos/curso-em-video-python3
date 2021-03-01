'''
    Crie um script que leia um valor em metros
    e o exiba convertido em cm e mm
'''

print('= '*6 + 'MEDIDAS' + ' ='*6)

metros = float(input('Informe a medida em metros: '))

print('cm: {}\nmm: {}'.format(metros*100, metros*1000))

print('= '*15)