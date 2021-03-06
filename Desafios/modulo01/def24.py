'''
    Crie um script que leia um nome de uma cidade e diga se ela começã ou nao com 'Santo' 
'''

print('= ' * 6 + 'NOME DE SANTO EUROPEU?' + ' =' * 6)

nome = input('Informe seu nome da cidade: ').strip()
print(nome[:5].lower() == 'santo')

print('= ' * 15)
