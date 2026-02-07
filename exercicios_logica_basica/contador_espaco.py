frase = input('Digite uma frase curta: ')

contador = 0
indice = 0

while indice < len(frase):
    letra = frase[indice]
    indice += 1
    if letra == ' ':
        contador += 1

if contador > 0:
    print(f'A quantidade de espaços na sua frase é {contador}')    
else:
    print(f'Sua frase não contém espaços') 