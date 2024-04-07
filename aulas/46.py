"""
0123456789
Ola mundo.

"""

variavel = 'Ola mundo.'

print(variavel[2:], ' - 1')
print(variavel[-2:], ' - 2')
print(variavel[5:9], ' - 3')
print(variavel[::-1], ' - 4')
print(variavel[:6], ' - 5')
print(variavel[0:9:2], ' - 6')
print(len(variavel))

nome = input('Digite seu nome \n')
idade = input('Qaul é a sua idade \n')

if(nome and idade != False):
    print(f'Seu nome é {nome}\nSeu nome invertido é {nome[::-1]}')

    if(' ' in nome):
        print('Seu nome Tem espaço')
    else:
        print('Seu nome Não tem espaço')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou um campo vazio!")