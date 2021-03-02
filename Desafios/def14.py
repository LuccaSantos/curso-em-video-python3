'''
    Crie um script que converta uma temperatura digitada em Cº para Fº
'''
print('= '*6 + 'TEMPERATURA' + ' ='*6)

celsius = float(input('Informe a temperatura em Celsius: '))
print('A temperatura em Fharenheit é: {}'.format((9/5*celsius)+32))

print('= '*15)