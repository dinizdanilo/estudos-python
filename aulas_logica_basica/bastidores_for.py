"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue um próximo valor
iter -> me entregue seu iterador
"""

# for letra in texto

texto = 'Danilo' # iterável
iteratador = iter(texto) # iterator 

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break