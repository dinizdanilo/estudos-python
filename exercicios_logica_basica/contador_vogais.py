frase = input('Digite uma frase simples: ')

contador = 0
indice = 0

while indice < len(frase):
    letra = frase[indice].lower
    indice += 1
    
    if letra == 'a':
        contador += 1
    elif letra == 'e':
        contador += 1
    elif letra == 'i':
        contador += 1
    elif letra == 'o':
        contador += 1
    elif letra == 'u':
        contador += 1
        
print(f'O número de vogais na sua frase é {contador}')        