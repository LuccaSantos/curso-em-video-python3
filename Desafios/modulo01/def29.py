'''
    Crie um script que leia a velocidade de um carro
    se ele ultrapassar 80km/h mostre uma mensagem dizendo q ele foi multado
    a multa custa 7$ por cada km acima do limite
'''

print('= ' * 6 + 'PRF' + ' =' * 6)

velocidade = float(input('Informe a velocidade do carro: '))
if velocidade > 80:
    print('Multona de {}$'.format((velocidade - 80) * 7))
else:
    print('Ta suave')

print('= ' * 15)
