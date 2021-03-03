'''
    Crie um script que leia 3 numeros e mostre qual é o maior e o menor
'''
print('= ' * 6 + 'MAIOR DOS 3' + ' =' * 6)

primeiro = float(input('Informe o primeiro número: '))
segundo = float(input('Informe o segundo número: '))
terceiro = float(input('Informe o terceiro número: '))
maior = 0
menor = 0
if (primeiro > segundo) and (segundo > terceiro):
    maior = primeiro
elif (segundo > primeiro) and (primeiro > terceiro):
    maior = segundo
else:
    maior = terceiro

if (primeiro < segundo) and (segundo < terceiro):
    menor = primeiro
elif (segundo < primeiro) and (primeiro < terceiro):
    menor = segundo
else:
    menor = terceiro
print('Maior: {}\nMenor: {}'.format(maior, menor))

print('= ' * 15)