frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.' 

i = 0
qtd_apareceu_mais = 0
letra_apareceu_mais = ''

while i < len(frase):
    letra_atual = frase[i].lower()
    qtd_apareceu_mais_atual = frase.count(letra_atual)
    
    if letra_atual == ' ':
        i += 1
        continue
    
    if qtd_apareceu_mais <= qtd_apareceu_mais_atual:
        qtd_apareceu_mais = qtd_apareceu_mais_atual
        letra_apareceu_mais = letra_atual
        
    i += 1
    
print(
    'A letra que apareceu mais vezes foi '
      f'"{letra_apareceu_mais}" que apareceu '
      f'{qtd_apareceu_mais}x'
      )