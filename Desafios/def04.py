'''
    Crie um script que leia algo pelo teclado e mostre
    na tela o seu tipo primitivo e todas as informações 
    possiveis sobre ela
'''
entrada = input('Digite algo: ')
print('O tipo de {0} é {1}'.format(entrada, type(entrada)))
print('{} é alfabeto?: {}'.format(entrada, entrada.isalpha()))
print('{} é numerico?: {}'.format(entrada, entrada.isnumeric()))
print('{} é alfanumerico?: {}'.format(entrada, entrada.isalnum()))
print('{} é somente espaços?: {}'.format(entrada, entrada.isspace()))
print('{} é decimal?: {}'.format(entrada, entrada.isdecimal()))
print('{} é digito?: {}'.format(entrada, entrada.isdigit()))
print('{} esta minúsculo?: {}'.format(entrada, entrada.islower()))
print('{} esta maiúsculo?: {}'.format(entrada, entrada.isupper()))