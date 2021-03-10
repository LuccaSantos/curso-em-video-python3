'''
    Crie um script q leia varios numeros inteiros, o programa so vai para quando 
    o usuario digitar o valor 999, no final mostre quantos números foram digitados 
    e qual foi a soma entre eles (desconsiderando o flag) 
'''

print('= ' * 6 + 'QUANTOS NÚMEROS FORAM DIGITADOS?' + ' =' * 6)

print('DIGITE 999 PARA ENCERRAR!')
numero_informado = 0
numero_de_inputs = 0
soma_numeros = 0
while numero_informado != 999:
    numero_informado = float(input('Informe o número que deseja: '))
    if numero_informado != 999:
        numero_de_inputs += 1
        soma_numeros += numero_informado

print('Quantidade de nº informados: {}\nSoma dos nº informados: {}'.format(
    numero_de_inputs, soma_numeros))

print('= ' * 15)
