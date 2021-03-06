'''
    Crie um script que leia o nome de uma pessoa e diga se ela tem ou nao 'Silva' no nome
'''
print('= '*6 + 'SILVA OU NAO' + ' ='*6)

auxiliar = input('Informe seu nome: ')
nome = auxiliar.lower()
print('O nome possui Silva: {}'.format('silva' in nome))

print('= '*15)