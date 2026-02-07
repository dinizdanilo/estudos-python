while True:
    
    primeiro_numero = input('Digite o primeiro número: ').strip()
    try:
        primeiro_numero = float(primeiro_numero)
    except ValueError:
        print('Digite um número válido.')
        continue
    
    segundo_numero = input('Digite o segundo número: ').strip()
    try:
        segundo_numero = float(segundo_numero)
    except ValueError:
        print('Digite um número válido.')
        continue
    
    print('\nEscolha uma das quatro operações\n'   
    'Adição (+)\n'
    'Subtração (-)\n'
    'Multiplicação (*)\n'
    'Divisão (/)\n'
    )
    
    operacao = input('\nEscolha uma das quatro operações: ').strip()
    
    if operacao == '+':
        resultado = primeiro_numero + segundo_numero
        print(f'\nO resultado da soma entre {primeiro_numero} e {segundo_numero} é igual a {resultado:.2f}')
    elif operacao == '-':
        resultado = primeiro_numero - segundo_numero
        print(f'\nO resultado da subtração entre {primeiro_numero} e {segundo_numero} é igual a {resultado:.2f}')
    elif operacao == '*':
        resultado = primeiro_numero * segundo_numero
        print(f'\nO resultado da multiplicação entre {primeiro_numero} e {segundo_numero} é igual a {resultado:.2f}')
    elif operacao == '/':
        if segundo_numero == 0:
            print('Não é possível dividir por zero!')
            continue
        resultado = primeiro_numero / segundo_numero
        print(f'\nO resultado da divisão entre {primeiro_numero} e {segundo_numero} é igual a {resultado:.2f}')
    else:
        print('Escolha uma operação válida!')   
        continue 
        
    opcao = input('Você deseja finalizar a calculadora?: ').lower().startswith('s')
    
    if opcao:
        print('Calculadora finalizada.')
        break