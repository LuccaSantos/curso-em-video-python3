'''
    Crie um script q leia o primeiro termo e a razao de uma PA. No final mostre os 10 primeiros termos dessa progressão
'''

print('= ' * 6 + 'PROGRESSÃO ARITMÉTICA' + ' =' * 6)

razao = int(input('Informe a razão da PROGRESSÃO ARITMÉTICA: '))
primeiro_termo = int(
    input('Informe o primeiro termo da PROGRESSÃO ARITMÉTICA: '))
for contador in range(primeiro_termo, (primeiro_termo + (11 - 1) * razao),
                      razao):
    print(contador)

print('= ' * 15)