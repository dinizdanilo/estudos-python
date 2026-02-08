frase = input('Digite uma frase: ')
letra_procurada = input('Escolha uma letra: ')

i = 0
contador = 0

while i < len(frase):
    letra_atual = frase[i].lower()
    i += 1
    
    if letra_atual == letra_procurada:
        contador += 1
        
print(f'Sua frase foi: {frase}')
print(f'A letra que você escolheu foi {letra_procurada}')        
print(f'A quantidade de vezes que sua letra aparece na frase foi {contador}x')        