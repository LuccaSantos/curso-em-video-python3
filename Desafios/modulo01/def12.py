'''
    Crie um script que leia o preço de um produto e mostre
    seu novo preço , com 5% de desconto
'''
print('= '*6 + 'CALCULADORA DE DESCONTOS' + ' ='*6)

produto = float(input('Informe o valor do produto R$: '))
print('O produto com desconto de 5% fica R$:{}'.format(produto - produto*0.05))

print('= '*15)
