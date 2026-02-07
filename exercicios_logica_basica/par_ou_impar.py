numero = input('Digite um número inteiro: ')

try:
    numero = int(numero)
    if numero % 2 == 0:
        print(f'O número {numero} que você digitou é par.')
    else:
        print(f'O número {numero} que você digitou é ímpar.')
except ValueError:
    print('O que você digitou não é um número inteiro.')