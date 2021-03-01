'''
    Crie um script que leia a largura e a altura de uma parede em metros,
    calcule a sua area e a quantidade de tinta necessaria
    para pinta-la, sabendo que cada litro de tinta pinta
    2m cubicos
'''
print('= '*6 + 'CALCULADORA PINTORES' + ' ='*6)

largura = float(input('Informe a largura em metros: '))
altura = float(input('Informe a altura em metros: '))
print('Vai precisar de {} litros de tinta para pintar {} metros quadrados de parede'.format(largura*altura/2, largura*altura))

print('= '*15)
