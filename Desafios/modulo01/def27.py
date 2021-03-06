'''
    Crie um script que leia o nome de uma pessoa e mostre o primeiro e ultimo nome separadamente
'''
print('= ' * 6 + 'PRIMEIRO E ULTIMO NOME' + ' =' * 6)

nome = input('Informe seu nome: ')
nome_separado = nome.split()
numero_de_palavras = len(nome_separado) - 1
print('Seu primeiro nome: {}\nSeu ultimo nome: {}'.format(
    nome_separado[0], nome_separado[numero_de_palavras]))

print('= ' * 15)
