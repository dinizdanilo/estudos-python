nome = input('Digite seu nome: ')

contagem = len(nome)

if contagem <= 4:
    print('Seu nome é curto')
elif contagem <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')         