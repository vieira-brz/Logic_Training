# 1 - Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a soma entre A e B e mostre se a soma é menor que C.

import sys

a = input('A: ')
if a.isdigit():
    a = float(a)
else:
    sys.exit('Not a number!')    

b = input('B: ')
if b.isdigit():
    b = float(b)
else:
    sys.exit('Not a number!')    

c = input('C: ')
if c.isdigit():
    c = float(c)
else:
    sys.exit('Not a number!')    

soma = a + b

print(f'{soma=}')
print(f'{soma=} é menor que C') if soma < c else ...