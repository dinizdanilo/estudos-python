frase = input('Digite uma frase simples: ')

contador = 0
indice = 0

while indice < len(frase):
    letra = frase[indice].lower()
    indice += 1
    
    if letra == ' ':
        continue
    
    if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u':
        contador += 1
        
print(f'O numero de consoantes na sua frase é {contador}')