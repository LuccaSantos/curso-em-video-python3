'''
    Crie um script que leia um nome de uma cidade e diga se ela começã ou nao com 'Santo' 
'''

print('= '*6 + 'NOME DE SANTO EUROPEU?' + ' ='*6)


nome = input('Informe seu nome da cidade: ')
nome_separado = nome.split()
if nome_separado[0] == 'Santo' or 'santo':
    print('Começa com Santo :/')
else:
    print('Não começa com Santo :D')

print('= '*15)