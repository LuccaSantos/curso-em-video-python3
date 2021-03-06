'''
    Crie um script que leia o peso e altura de uma pessoa, calcule o seu IMC e mostre seu status de acordo com a tabela abaixo:
    - abaixo de 18.5: Abaixo do peso
    - entre 18.5 e 25: Peso ideal
    - entre 25 e 30: Sobrepeso
    - entre 30 e 40: Obesidade
    - acima de 40: Obesidade morbida 
'''
print('= ' * 6 + 'CALCULO IMC' + ' =' * 6)

altura = float(input('Informe a altura da pessoa: '))
peso = float(input('Informe o peso da pessoa: '))
imc = peso / altura**2
if (imc < 18.5):
    print('Abaixo do peso')
elif (imc >= 18.5) and (imc < 25):
    print('Peso ideal')
elif (imc >= 25) and (imc < 30):
    print('Sobrepeso')
elif (imc >= 30) and (imc < 40):
    print('Obesidade')
elif (imc >= 40):
    print('Obesidade morbida')

print('= ' * 15)