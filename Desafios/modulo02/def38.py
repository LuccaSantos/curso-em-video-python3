'''
    Crie um script q leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem
    - O primeiro valor é maior
    - O segundo valor é maior 
    - Não existe valor maior, os dois sao iguais
'''
print('= ' * 6 + 'MAIOR, MENOR OU IGUAL' + ' =' * 6)

primeiro = float(input('Informe o primeiro número: '))
segundo = float(input('Informe o segundo número: '))
if (primeiro > segundo):
    print('O Primeiro valor é o maior!')
elif (segundo > primeiro):
    print('O segundo valor é o maior!')
else:
    print('Os valores são iguais!')
print('= ' * 15)