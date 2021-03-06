'''
    Crie um script q leia o ano de nascimento de um jovem e informe de acordo com sua idade:
    - se ele ainda vai se alistar no exercito
    - se é a hora de se alistar
    - se ja passou do tempo de se alistar
    - e mostrar o tempo q falta ou passou
'''
print('= ' * 6 + 'ALISTAMENTO OBRIGATORIO' + ' =' * 6)

nascimento = int(input('Informe seu ano de nascimento: '))
idade = 2021 - nascimento
if (idade < 18):
    print('Faltam {} anos para vc se alistar!'.format(18 - idade))
elif (idade == 18):
    print('Já está na hora de se alistar!')
else:
    print('Já passou {} anos de se alistar'.format(idade - 18))
print('= ' * 15)