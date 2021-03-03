'''
    Crie um script que leia uma frase pelo teclado e mostre:
    - A Quantidade de letras 'a'
    - em que posição ela aparece a primera vez
    - em que posicao ela aparece a ultima vez
'''

print('= ' * 6 + 'ANALISE DE FRASE' + ' =' * 6)

frase = input('Informe uma frase: ')
print(
    'Quantidade de letras a: {}\nPosição da primeira: {}\nPosição da ultima: {}'
    .format(frase.count('a'), 1 + frase.find('a'), 'a'))

print('= ' * 15)
