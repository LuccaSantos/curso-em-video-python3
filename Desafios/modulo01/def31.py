'''
    Crie um script que leia uma distancia em km e calcule o preço da passagem, cobrando 0.5$ por km
    para viagens de ate 200km e 0.45$ para viagens mais longas  
    
'''

print('= ' * 6 + 'AGENCIA DE VIAGENS' + ' =' * 6)

km = float(input('Informe a distancia da viagem em km: '))
if (km < 200):
    print('Vai pagar: {}$'.format(km * 0.5))
else:
    print('Vai pagar: {}$'.format(km * 0.45))

print('= ' * 15)