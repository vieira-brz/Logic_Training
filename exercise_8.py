# 8 - Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente.

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

ordem = [a, b, c]
ordem.sort(reverse=True)

print(ordem)