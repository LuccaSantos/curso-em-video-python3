'''
    Crie um script que jogue par ou impar com o computador,
    o programa encerra quando o jogador perder mostrando
    o total de vitorias
'''
import random

print('= ' * 6 + 'PAR OU ÍMPAR version 0.2' + ' =' * 6)
sequencia = 0
while True:
    escolha_jogador = int(input('[1] - PAR\n[2] - ÍMPAR\n'))
    numero_pc = random.randrange(0, 11)
    numero_jogador = int(input('Informe um número de 0 a 10: '))
    if ((numero_pc + numero_jogador) % 2 == 0) and escolha_jogador == 1:
        sequencia += 1
        print(f'{numero_jogador} + {numero_pc} é PAR, VOCE GANHOU!')
    elif ((numero_pc + numero_jogador) % 2 == 0) and escolha_jogador == 2:
        print(
            f'{numero_jogador} + {numero_pc} é PAR, VOCE PERDEU!\nSequência de vitorias: {sequencia}')
        break
        print(f'Sequência de vitorias: {sequencia}')
    elif ((numero_pc + numero_jogador) % 2 != 0) and escolha_jogador == 1:
        print(
            f'{numero_jogador} + {numero_pc} é ÍMPAR, VOCE PERDEU!\nSequência de vitorias: {sequencia}')
        break
    elif ((numero_pc + numero_jogador) % 2 != 0) and escolha_jogador == 2:
        sequencia += 1
        print(f'{numero_jogador} + {numero_pc} é ÍMPAR, VOCE GANHOU!')
    else:
        print('INFORME UMA OPÇÃO VALIDA!')


print('= ' * 15)
