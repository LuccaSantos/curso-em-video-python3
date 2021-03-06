'''
    Crie um script que leia o nome completo de uma pessoa e mostre:
    - nome todo em maiusculo e minusculo
    - quantos CARACTERES tem o nome
    - quantas letras tem o primeiro nome
'''
print('= '*6 + 'ANALISE DO SEU NOME' + ' ='*6)


nome = input('Informe seu nome: ')
primeiro_nome = nome.split()
print('Maiúsculo {}\nMinúsculo: {}\nNº de caracteres: {}\nNº de letras do primeiro nome: {}'.format(
    nome.upper(),
    nome.lower(),
    len(nome),
    len(primeiro_nome[0])
))


print('= '*15)