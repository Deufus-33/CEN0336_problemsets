#!/usr/bin/env python3
mensagem = '' # cria uma variavel vazia 
for x in (1,2,3,4,5):
    if x > 4:
        print("olá")
        mensagem = 'x é grande'
    else:
        print(x)
        mensagem = 'x é pequeno'
    print(mensagem)
print('feito!')
