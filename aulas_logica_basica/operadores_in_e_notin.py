# Operadores in e not in
# Strings são iteráveis
#   0 1 2 3 4 5
#   D a n i l o
#  -6-5-4-3-2-1
# nome = 'Danilo'
# print(nome[2])
# print(nome[-4])
# print('a' in nome)
# print('zero' in nome)
# print (10 * '-')
# print('Dan' not in nome)
# print('z' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')