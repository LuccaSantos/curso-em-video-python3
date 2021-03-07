'''
    Crie um script q leia uma frase qualquer e diga se ela é um palindromo desconsiderando os espaços
'''

print('= ' * 6 + 'PALINDROMO' + ' =' * 6)

frase = input('Informe a frase: ').strip().lower().replace(' ', '')
frase_invertida = frase[::-1]
if (frase == frase_invertida):
    print('É PALINDROMO!')
else:
    print('NÃO É PALINDROMO!')

print('= ' * 15)
