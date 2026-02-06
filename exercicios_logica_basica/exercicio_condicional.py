nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

# if nome == '' or idade == '':
#     print('Desculpe, você deixou campos vazios.')
# else:
#     print(f'Seu nome é {nome}')    
#     print(f'Seu nome ao contrário é {nome[::-1]}')
#     print(f'Seu nome tem {len(nome)} letras')
#     if ' ' in nome:
#         print('Seu nome contém espaços.')
#     else:
#         print('Seu nome não contém espaços.')
#     print(f'A primeira letra do seu nome é {nome[0]}')
#     print(f'A ultima letra do seu nome é {nome[-1]}') 

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome ao contrário é {nome[::-1]}')
    print(f'Seu nome tem {len(nome)} letras') 
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome não contém espaços.')
else:
    print('Desculpe, você deixou campos vazios.')         