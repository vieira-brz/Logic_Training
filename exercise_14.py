# 14 - Faça um algoritmo que receba um valor A e B, e troque o valor de A por B e o valor de B por A e imprima na tela os valores.

a = input('A: ')
b = input('B: ')

print(f'Antes: {a=} e {b=}')

c = a
a = b
b = c

print(f'Depois: {a=} e {b=}')