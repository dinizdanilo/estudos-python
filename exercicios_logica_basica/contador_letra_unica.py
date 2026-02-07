frase = input('Digite uma frase: ')

contador_letra_a = 0
indice = 0

while indice < len(frase):
    letra_a = frase[indice].lower()
    indice += 1
    
    if letra_a != 'a':
        continue
    else:
        contador_letra_a += 1
  
print(f'A quantidade de letras A na sua frase é {contador_letra_a}')