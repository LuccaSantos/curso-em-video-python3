'''
    Refaça o desafio 51 lendo o primeiro termo e a razao de uma PA monstrando os 
    10 primeiro termos da PA usando a estrutura while
'''

print('= ' * 6 + 'PROGRESSÃO ARITMÉTICA versao: 0.2' + ' =' * 6)

razao = int(input('Informe a razão da PROGRESSÃO ARITMÉTICA: '))
primeiro_termo = int(
    input('Informe o primeiro termo da PROGRESSÃO ARITMÉTICA: '))
termo_atual = primeiro_termo
contador = 1
while contador < 11:
    print(termo_atual)
    termo_atual += razao
    contador += 1

print('= ' * 15)
