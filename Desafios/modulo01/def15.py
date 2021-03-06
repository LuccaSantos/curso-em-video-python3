'''
    Crie um script que leia uma quantidade de km e quantidade de dias que um carro foi alugado e calcule o preço a pagar.
    sabendo q o carro custa $60 por dia e $0,15 por km rodado 
'''
print('= '*6 + 'ALUGUEL VIATURA' + ' ='*6)

km = float(input('Informe quantos km fora rodados: '))
dias = float(input('Informe quantos dias o carro foi usado: '))
print('O valor do aluguel é ${}'.format(km*0.15+dias*60))

print('= '*15)