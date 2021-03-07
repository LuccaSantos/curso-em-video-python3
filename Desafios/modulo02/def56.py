'''
    Crie um script q leia nome, idade e sexo de 4 pessoas, no final mostre:
    - a media de idade do grupo:
    - nome do homem mais velho 
    - quantas mulheres tem menos de 20 
'''

print('= ' * 6 + 'INFO PESSOAS' + ' =' * 6)

soma_idades = 0
homem_mais_velho = ''
numero_mulheres_menos_vinte = 0

for contador in range(1, 5):
    nome = input('Informe o nome: ')
    idade = int(input('Informe a idade: '))
    sexo = input('Informe o sexo: \n[M] - masculino\n[F] - feminino\n').upper()
    mais_velho = 0
    #homem mais velho
    if (mais_velho < idade) and (sexo == 'M'):
        homem_mais_velho = nome
    #mulheres com menos de vinte
    if (idade < 20) and (sexo == 'F'):
        numero_mulheres_menos_vinte += 1
    #media de idade
    soma_idades += idade

print('Media de idade: {}\nMulheres com menos de vinte: {}\nHomem mais velho: {}'.format(soma_idades / 4, numero_mulheres_menos_vinte, homem_mais_velho))

print('= ' * 15)