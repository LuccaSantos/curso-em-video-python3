'''
    Crie um script que leia um número inteiro 
    e mostre o seu sucessor e antecessor
'''
print('= '*6 + 'ANTES E DEPOIS' + ' ='*6)

numero = int(input('Informe um número:  '))
print('O seu antecessor é: {}\nO seu sucessor é: {:^5}'.format(numero-1, numero+1))

print('= '*20)