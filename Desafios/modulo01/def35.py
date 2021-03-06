'''
    Crie um script que leia o comprimento de 3 retas e diga para o usuario 
    se elas podem ou nao formar um triangulo 
'''
print('= ' * 6 + 'PRINCIPIO DO TRIANGULO' + ' =' * 6)

lado1 = float(input('Informe o comprimento de um lado: '))
lado2 = float(input('Informe o comprimento de um lado: '))
lado3 = float(input('Informe o comprimento de um lado: '))
if ((lado1 + lado2) > lado3 and (lado1 + lado3) > lado2
        and (lado2 + lado3) > lado1):
    print('Pode formar um triangulo!')
else:
    print('Não pode formar um triangulo!')

print('= ' * 15)