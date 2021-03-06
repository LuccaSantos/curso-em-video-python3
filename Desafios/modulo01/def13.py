'''
    Crie um script que leia o salario de um funcionario 
    e calcule o novo salario, com um aumento de 15%.
'''
print('= '*6 + 'CALCULADORA DE AJUSTES' + ' ='*6)

salario = float(input('Informe o valor do salario R$: '))
print('O salario com aumento de 15% fica R$:{}'.format(salario + salario*0.15))

print('= '*15)