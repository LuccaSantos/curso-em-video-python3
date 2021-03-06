'''
    Crie um script que leia quanto dinheiro uma pessoa tem
    e exiba quantos dolares ela pode comprar
    considerar: U$:1,00 = R$:5,30
'''

print('= '*6 + 'TRANSFERWISE DA DEEPWEB' + ' ='*6)

real = float(input('Informe a quantidade de reais: '))
print('Na cotação de R$:5,30 pode comprar: U$:{:.3f}'.format(real/5.30))


print('= '*15)
