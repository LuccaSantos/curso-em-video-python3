'''
    Crie um script 
'''
import random
import emoji
import time

from emoji.unicode_codes import es

print('= ' * 15)
print(emoji.emojize('PEDRA PAPEL TESOURA'))
print('= ' * 15)

nome_jogador = input('Informe o nome do jogador: ')
escolha_jogador = int(input('[1] - PEDRA\n[2] - PAPEL\n[3] - TESOURA\n'))
vencedor = ''
escolha_computador = random.randrange(1, 3)

if (escolha_jogador == escolha_computador):
    vencedor = 'empate'
else:
    if (escolha_computador == 1) and (escolha_jogador == 2):
        vencedor = 'jogador'
    elif (escolha_computador == 2) and (escolha_jogador == 1):
        vencedor = 'computador'
    elif (escolha_computador == 1) and (escolha_jogador == 3):
        vencedor = 'computador'

    elif (escolha_computador == 3) and (escolha_jogador == 1):
        vencedor = 'jogador'

    elif (escolha_computador == 2) and (escolha_jogador == 3):
        vencedor = 'jogador'

    elif (escolha_computador == 3) and (escolha_jogador == 2):
        vencedor = 'computador'

print('JO')
time.sleep(1)
print('KE')
time.sleep(1)
print('PO')

if (escolha_computador == 1) and (escolha_jogador == 2):
    print('COMPUTADOR: PEDRA\n{}: PAPEL'.format(nome_jogador.upper()))
elif (escolha_computador == 2) and (escolha_jogador == 1):
    print('COMPUTADOR: PAPEL\n{}: PEDRA'.format(nome_jogador.upper()))
elif (escolha_computador == 1) and (escolha_jogador == 3):
    print('COMPUTADOR: PEDRA\n{}: TESOURA'.format(nome_jogador.upper()))
elif (escolha_computador == 3) and (escolha_jogador == 1):
    print('COMPUTADOR: TESOURA\n{}: PEDRA'.format(nome_jogador.upper()))
elif (escolha_computador == 2) and (escolha_jogador == 3):
    print('COMPUTADOR: PAPEL\n{}: TESOURA'.format(nome_jogador.upper()))
elif (escolha_computador == 3) and (escolha_jogador == 2):
    print('COMPUTADOR: TESOURA\n{}: PAPEL'.format(nome_jogador.upper()))

if (vencedor == 'empate'):
    print('- ' * 10)
    print(emoji.emojize('EMPATE \U0001F643'))
    print('- ' * 10)
elif (vencedor == 'jogador'):
    print('- ' * 10)
    print(emoji.emojize('{} VENCEU! \U0001F609'.format(nome_jogador)))
    print('- ' * 10)
else:
    print('- ' * 10)
    print(emoji.emojize('COMPUTADOR VENCEU! \U0001F601'))
    print('- ' * 10)



print('= ' * 15)
