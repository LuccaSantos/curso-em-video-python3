'''
    Crie um script que aprova emprestimo para compra de imoveis, leia o valor da casa, o salario do comprador e em 
    quantos anos ele vai pagar, calcule o valor da mensalidade, sabendo que ela nao pode exceder 30% do salario!
'''
print('= ' * 6 + 'EMPRESTIMO IMOBILIARIO' + ' =' * 6)

salario = float(input('Informe o valor do seu salário: '))
valor_imovel = float(input('Informe o valor do imovel: '))
tempo = float(input('Informe em quantos anos quer pagar o imovel: '))
mensalidade = valor_imovel / (tempo * 12)
if (mensalidade > (salario * 0.3)):
    print('Infelizmente nao pode financiar o barraco!')
else:
    print('Pode financiar a goma, com mensalidade de {}$'.format(mensalidade))

print('= ' * 15)