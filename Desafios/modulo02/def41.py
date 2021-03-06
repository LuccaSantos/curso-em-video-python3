'''
    Crie um script que leia o ano de nascimento de um atleta e mostre sua 
    categoria de acordo com sua idade:
    - ate 9 : mirim
    - ate 14: infantil
    - ate 19: junior
    - ate 20: senior
    - acima : master
'''
print('= ' * 6 + 'CATEGORIA DE ATLETA' + ' =' * 6)

nascimento = int(input('Informe seu ano de nascimento: '))
idade = 2021 - nascimento
if (idade <= 9):
    print('MIRIM')
elif (idade > 9) and (idade <= 14):
    print('INFANTIL')
elif (idade > 14) and (idade <= 19):
    print('JUNIOR')
elif (idade == 20):
    print('SENIOR')
else:
    print('MASTER')

print('= ' * 15)