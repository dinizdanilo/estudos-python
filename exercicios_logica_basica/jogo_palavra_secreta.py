palavra_secreta = ('automovel')

letras_acertadas = ''
tentativas = 0
palavra_formatada = ''

while palavra_formatada != palavra_secreta:
    palavra_formatada = ''
    letra_digitada = input('Digite uma letra: ').lower()
    
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    
    tentativas += 1
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
            
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formatada += letra_secreta
        else:
            palavra_formatada += '*'   
            
    if tentativas == 6:
        print('Você perdeu!\n'
              f'A palavra secreta era "{palavra_secreta}"')
        break        
           
    print(palavra_formatada)
            
    print('VOCÊ GANHOU PARABENS!!\n'
    f'A palavra secreta era: "{palavra_secreta}"\n' 
    f'A quantidade de tentativas foi: {tentativas}')        