frase = input('Digite uma frase: ')

contador_vogais = 0
contador_numeros = 0
contador_consoantes = 0
contador_espaços = 0

indice = 0

while indice < len(frase):
    letra = frase[indice].lower()
    indice += 1
    
    if letra == ' ':
        contador_espaços += 1
    elif letra.isdigit():
        contador_numeros += 1
    elif letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        contador_vogais += 1
    elif letra.isalpha():
        contador_consoantes += 1
    
     
print(f'A quantidade de vogais na sua frase é igual a {contador_vogais}')
print(f'A quantidade de consoantes na sua frase é igual a {contador_consoantes}')
print(f'A quantidade de números na sua frase é igual a {contador_numeros}')
print(f'A quantidade de espaços na sua frase é igual a {contador_espaços}')