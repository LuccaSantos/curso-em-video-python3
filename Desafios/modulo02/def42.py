'''
    Crie um script baseado no exercicio 35, se puder formar um triangulo e diga se o triangulo é:
    - equilatero (lados iguais), isosceles (dois lados iguais) ou escaleno (todos lados diferentes)
'''
print('= ' * 6 + 'EQUILATERO, ISOSCELES E ESCALENO' + ' =' * 6)

lado1 = float(input('Informe o comprimento de um lado: '))
lado2 = float(input('Informe o comprimento de um lado: '))
lado3 = float(input('Informe o comprimento de um lado: '))
if ((lado1 + lado2) > lado3 and (lado1 + lado3) > lado2
        and (lado2 + lado3) > lado1):
    if (lado1 == lado2) and (lado2 == lado3):
        print('Formar um triangulo equilatero!')
    elif (lado1 == lado2) or (lado2 == lado3) or (lado1 == lado3):
        print('Formar um triangulo isosceles!')
    else:
        print('Formar um triangulo escaleno!')
else:
    print('Não pode formar um triangulo!')

print('= ' * 15)