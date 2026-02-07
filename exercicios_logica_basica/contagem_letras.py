nome = input('Digite seu nome: ')

contagem = len(nome)

if contagem > 1:
    if contagem <= 4:
        print('Seu nome é curto')
    elif contagem <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de 1 letra.')                 