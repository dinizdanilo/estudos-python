frase = input('Digite uma frase: ')
nova_frase = ''

i = 0

while i < len(frase):
    letra_atual = frase[i].lower()
    i += 1
    
    if letra_atual in 'aeiou':
        nova_frase = nova_frase + '*'
    else:
        nova_frase = nova_frase + letra_atual    

print(f'Original: {frase} ')
print(f'Censurada: {nova_frase}')