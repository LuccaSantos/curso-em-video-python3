'''
    Crie um script q leia seis numeros inteiro e mostre a soma dos pares 
'''

print('= ' * 6 + 'SOMA DOS PARES' + ' =' * 6)

soma_dos_pares = 0
for contador in range(1, 7):
    numero = int(input('Informe um número inteiro: '))
    if (numero % 2 == 0):
        soma_dos_pares += numero
print('A soma do números pares é {}'.format(soma_dos_pares))

print('= ' * 15)