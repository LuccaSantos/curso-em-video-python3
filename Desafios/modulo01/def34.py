'''
    Crie um script q pergunte o salario de um funcionario e calcule o valor do seu aumtento.
    para salarios superiores a 1250$ calcule 10%
    para inferiores ou iguais calcule 15%
'''
print('= ' * 6 + 'AUMENTO SALARIAL' + ' =' * 6)

salario = float(input('Informe seu salário: '))
if (salario > 1250):
    salario += salario * 0.1
else:
    salario += salario * 0.15
print('O seu novo salario é: {}'.format(salario))

print('= ' * 15)