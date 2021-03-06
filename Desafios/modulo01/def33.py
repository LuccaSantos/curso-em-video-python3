'''
    Crie um script que leia 3 numeros e mostre qual é o maior e o menor
'''
print('= ' * 6 + 'MAIOR DOS 3' + ' =' * 6)

primeiro = float(input('Informe o primeiro número: '))
segundo = float(input('Informe o segundo número: '))
terceiro = float(input('Informe o terceiro número: '))
maior = primeiro
if (segundo > primeiro) and (primeiro > terceiro):
    maior = segundo
if (terceiro > segundo) and (segundo > primeiro):
    maior = terceiro
menor = primeiro
if (segundo < primeiro) and (primeiro < terceiro):
    menor = segundo
if (terceiro < primeiro) and (primeiro < segundo):
    menor = terceiro
print('Maior: {}\nMenor: {}'.format(maior, menor))

print('= ' * 15)