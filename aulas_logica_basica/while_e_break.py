"""
Repetições 
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
Operadores de atribuição
= += -= *= /= //= **= %=
"""

# condicao = True

# while condicao:
#     nome = input('Qual o seu nome? ')
#     print(f'Seu nome é {nome}')
    
#     if nome == 'Sair':
#         break

# print('Acabou')    

# contador = 0

# while contador < 10:
#     contador = (contador + 1)
#     print(contador)

# print('Acabou')   
 
# contador = 10

# contador *= 2
# print(contador)

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6')
        continue
    
    if contador <= 10 and contador <= 27:
        print('Não vou mostar o ', contador)
        continue
    
    print(contador)
    
    if contador == 40:
        break
    
print('Acabou')     

