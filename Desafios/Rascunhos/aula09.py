#manipulando strings

frase = 'Curso em video python'
#fatiamento
print(frase[9:14])
print(frase[9:14:2])
print(frase[:5])
print(frase[6:])
print(frase[9::3])
print(frase[::3])
#analise
print(len(frase)) #numero de caracteres
print(frase.count('o')) #conta letras 'o'
print(frase.count('o', 0, 13)) #conta de caracteres + fatiamento'
print(frase.find('deo')) #retorna posicao 
print('Curso'in frase) #retorna boolean
#transformacao
print(frase.replace('python', 'Android')) #substitue
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
frase1 = '   Aprender python  '
print(frase1.strip()) #remover espacos inuteis
print(frase1.rstrip()) #right
print(frase1.lstrip()) #left
#divisao
print(frase.split()) #separa a cadeia em palavras com base no espaco
#juncao
print('-'.join(frase)) #junta a cadeia separando palavras por -
