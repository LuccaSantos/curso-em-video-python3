'''
    Crie um script que calcule o valor a ser pago por um produto, considerando o seu preco normal e condição de pagamento:
    - á vista dinheiro/cheque: 10% de desconto
    - a vista no cartão: 5% de desconto
    - em até 2x no cartão: preco normal
    - 3x ou mais no cartao: 20% de juros
'''
print('= ' * 6 + 'DESCONTOS' + ' =' * 6)

preco_produto = float(input('Informe o preço do produto: '))
novo_preco = 0
modo_pagamento = int(
    input(
        '[1] - Á vista no dinheiro/cheque\n[2] - Á vista no cartão\n[3] - Em até 2x no cartão\n[4] - 3x ou mais no cartão: '
    ))
if (modo_pagamento == 1):
    novo_preco = preco_produto - preco_produto * 0.1
    print('O produto ficará por: {}'.format(novo_preco))
elif (modo_pagamento == 2):
    novo_preco = preco_produto - preco_produto * 0.05
    print('O produto ficará por: {}'.format(novo_preco))
elif (modo_pagamento == 3):
    print('O produto ficará por: {}'.format(preco_produto))
else:
    novo_preco = preco_produto + preco_produto * 0.2
    print('O produto ficará por: {}'.format(novo_preco))

print('= ' * 15)