numero = input('Digite um número inteiro: ')

try:
    numero = int(numero)
    if numero % 2 == 0:
        print('O número que você digitou é par.')
    else:
        print('O número que você digitou é ímpar.')
except ValueError:
    print('O que você digitou não é um número inteiro.')