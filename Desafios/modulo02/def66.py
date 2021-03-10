'''
    crie um script q leia varios numeros inteiros (flag 999)
    no final mostre quantos números foram digitados e qual a 
    soma entre eles
'''

print('= ' * 6 + 'TESTANDO O BREAK' + ' =' * 6)

soma = 0
numero_inputs = 0
while True:
    numero_atual = float(input('Informe um número(999 para para!): '))
    if numero_atual == 999:
        break
    else:
        soma += numero_atual
        numero_inputs += 1
print(f'A soma dos {numero_inputs} numeros digitados é {soma}')

print('= ' * 15)
