nome = input('Digite seu nome: ')

indice = len(nome) -1
nome_invertido = ''

while indice >= 0:
    letra = nome[indice]
    nome_invertido += letra
    indice -= 1
    
    continue

print(f'Seu nome invertido é {nome_invertido}')