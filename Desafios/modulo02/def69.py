'''
    Crie um script q leia a idade e o sexo de varias pessoas
    a cada pessoa cadastrada o script deve perguntar se o usuario 
    quer continuar, no final mostre
        - quantas pessoas tem mais de 18
        - quantos sao homens 
        - quantas sao mulheres e tem menos de 20 anos
'''

print('= ' * 6 + 'CONTAGEM DE PESSOAS' + ' =' * 6)

continuar = 's'
numero_de_maiores = 0
numero_de_homens = 0
numero_de_mulheres_abaixo_de_20 = 0
while continuar != 'n':
    idade = int(input('Informe sua idade: '))
    sexo = int(input('Informe seu sexo\n[1] - MASCULINO\n[2] - FEMININO'))
    # contagem dos maiores de idade
    if (idade >= 18):
        numero_de_maiores += 1
    # contagem dos homens
    if (sexo == 1):
        numero_de_homens += 1
    # contagem das mulheres...
    if (sexo == 2) and (idade < 20):
        numero_de_mulheres_abaixo_de_20 += 1
    continuar = input('Deseja continuar? [s/n]').lower()
print(
    f'Maiores de idade: {numero_de_maiores}\nHomens: {numero_de_homens}\nMulheres com menos de 20: {numero_de_mulheres_abaixo_de_20}')

print('= ' * 15)
