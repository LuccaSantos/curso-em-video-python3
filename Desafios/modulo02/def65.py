'''
    Crie um script q leia varios numeros e no final da execução
    mostre a media dos valores e qual foi o maior e o menor valor
    o script tbm deve perguntar ao usuario se ele quer continuar a 
    digitar valores
'''

print('= ' * 6 + 'MAIOR, MENOR E MEDIA' + ' =' * 6)


continuar = 's'
while continuar != 'n':
    soma_numeros = 0
    numero_inputs = 0
    maior = 0
    menor = 0
    numero_atual = 0
    while numero_atual != 999:
        numero_atual = float(input('Informe um número: '))
        if numero_atual != 999:
            # maior e menor
            if numero_inputs == 0:
                maior = numero_atual
                menor = numero_atual
            else:
                if numero_atual > maior:
                    maior = numero_atual
                elif numero_atual < menor:
                    menor = numero_atual
            # media
            numero_inputs += 1
            soma_numeros += numero_atual

    print('Media dos valores: {}\nMaior: {}\nMenor: {}'.format(
        soma_numeros/numero_inputs, maior, menor))
    continuar = input('Deseja continuar?: [s/n]').lower()

print('= ' * 15)
