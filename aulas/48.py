valorEntrada = input('Digite um numer: ')

try:
    numeroEntrada = float(valorEntrada)
    print(f'Float: {numeroEntrada}')
    print(f'O dobro de {numeroEntrada} é {numeroEntrada * 2}')
except:
    print('Isso não é um numero!')