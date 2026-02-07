frase = input('Digite uma frase simples: ')

contador = 0
indice = 0

while indice < len(frase):
    letra = frase[indice]
    indice += 1 
    
    if letra.isdigit():
        continue
    elif letra == ' ':
        continue
    
    contador += 1
    
    
print(f'A quantidade de letras que a frase tem é {contador}')    