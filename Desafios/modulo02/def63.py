'''
    Crie um script q leia um numero n inteiro qualquer e mostre
    na tela os n primeiros elementos de uma sequencia de fibonacci   
'''

print('= ' * 6 + 'FIBONACCI' + ' =' * 6)

numero = int(input('Informe quantos termos deseja ver: '))
aux1 = 1
aux2 = aux1
aux3 = int
print(aux1)
while numero >= 1:
    print(aux2)
    aux3 = aux2
    aux2 = aux1 + aux2
    aux1 = aux3
    numero -= 1

print('= ' * 15)
