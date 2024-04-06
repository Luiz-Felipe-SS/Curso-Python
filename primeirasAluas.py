adicao = 2 + 2
print ('adicao: ', adicao)

sub =  4 - 4
print ('subtração : ', sub)

mult = 8 * 8
print ('multiplicação: ', mult)

divi = 160 / 16.2
print('divisão: ', divi)

divi_inteiro = 160   // 16.2
print('divisão inteira: ', divi_inteiro)

expon = 2 ** 10
print('Exponenciação', expon)

modulo = 25 % 5 
print('modulo', modulo)

concatenacao = 'A' + 'B' + 'C' + 'D' 
print(concatenacao)

repeticao = 'A' * 15
print(repeticao)

repeticao2 = 'LUIZ ' * 15
print(repeticao2)

nome = 'Rodrigo'
peso = 95
altura = 1.80


# trabalhando com foratação


calcula = peso / (altura * altura)

print('IMC de ', nome, 'e: ', calcula)

linha_1 = f'{nome} tem {altura:.3f}, {peso:.2f} e IMC de {calcula:.2f}'

print(linha_1)

a1 = 'AAAAA'
b1 = 'BBBBB'
c1 = 'CCCCC'
d1 = 10.895

string = 'FORMATACAO a1= {}, b1 = {}, c1 = {}, d1 = {:.2f} '
print(string.format(a1, b1, c1, d1))

print(60 * '=')
print(60 * '=')

teste = input('Qual seu nome? ')
print(f'Seu nome é {teste}')                    

primeiroIf = input('Digite uma entrada: ')

if primeiroIf == 'oi':
    print('oi')

elif primeiroIf == 'ola':
    print('Ola')
else:
    print('Errouuu')
print('saiu')

valor1 = input('Valor 1: ')
valor2 = input('Valor 2: ')


if valor1 >= valor2:
    print(f'{valor1=} é maior')
else:
    print(f'{valor2=} é maior.')

entrada = input('[E] para entrar - [S] para sair: ')
valorSenha = input('Digite uma senha: ')

senha_permitida = '123456789'

if(entrada =='E' and valorSenha == senha_permitida):
    print('Booooooooaaaaaaaaaa')
else:
    print("Deu ruim, senha errada")


























































