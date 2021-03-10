'''
    Crie um script q mostre a tabuada de varios números um de cada vez
    para cada valor digitado pelo usuario. (flag numero negativo)
'''

print('= ' * 6 + 'TABUADA Verion 0.2' + ' =' * 6)

while True:
    numero = int(input('Informe o número da tabuada(-1 para encerrar): '))
    if numero < 0:
        break
    else:
        contador = 1
        while contador <= 10:
            print(f'{numero} * {contador} = {numero * contador}')
            contador += 1
print('= ' * 15)
