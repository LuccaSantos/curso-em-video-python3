'''
    Melhore o exercicio 61, perguntando ao usuario se ele quer mostrar mais alguns termos
    o programa encerra quando ele disser q quer mostrar 0 termos
'''

print('= ' * 6 + 'PROGRESSÃO ARITMÉTICA Versao: 0.3' + ' =' * 6)

razao = int(input('Informe a razão da PROGRESSÃO ARITMÉTICA: '))
primeiro_termo = int(
    input('Informe o primeiro termo da PROGRESSÃO ARITMÉTICA: '))
ultimo_termo = 11
while ultimo_termo != 0:
    termo_atual = primeiro_termo
    contador = 1
    while contador < ultimo_termo:
        print('{}º termo: {}'.format(contador, termo_atual))
        termo_atual += razao
        contador += 1
    ultimo_termo = int(input('Deseja ver mais quantos termos?: ')) + 1

print('= ' * 15)
