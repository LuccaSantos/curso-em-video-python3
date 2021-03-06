'''
    Crie um script q leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final
    de acordo com a media atingida: 
    - media abaixo de 5.0 : reprovado
    - media entre 5 e 6.9 : reculperação
    - media 7 ou superior : aprovado
'''
print('= ' * 6 + 'MEDIA ESCOLAR' + ' =' * 6)

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2
if (media <= 5):
    print('REPROVADO!')
elif (media > 5) and (media < 6.9):
    print('RECULPERAÇÃO!')
else:
    print('APROVADO!')

print('= ' * 15)