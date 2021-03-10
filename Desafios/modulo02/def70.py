'''
    Crie um script q leia o nome e o preco de varios produtos, 
    o script deve perguntar se o usuario quer continuar e ao final:
        - qual é o total gasto na compra
        - quantos produtos custam mais de 1000
        - qual e o nome do produto mais barato
'''

print('= ' * 6 + '' + ' =' * 6)

total = 0
produtos_mais_de_mil = 0
produto_mais_barato = 'teste'
while True:
    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preco do produto: '))
    total += preco
    if (preco > 1000):
        produtos_mais_de_mil += 1
    contador = 1
    valor_do_mais_barato = float
    if (contador == 1):
        produto_mais_barato = nome
        valor_do_mais_barato = preco
    elif (preco < valor_do_mais_barato):
        produto_mais_barato = nome
    continuar = int(input('Deseja continuar?\n[1] - sim\n[999] - não\n'))
    if continuar == 999:
        break
    contador += 1
print(
    f'Produto mais barato: {produto_mais_barato}\nProdutos que custam mais de mil: {produtos_mais_de_mil}\nTotal: {total}')

print('= ' * 15)
