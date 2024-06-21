'''
3 - Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e B forem iguais, deverá somar os dois valores, 
caso contrário devera multiplicar A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado a uma variável C e
imprimir seu valor na tela.
'''

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

res = 0
if a == b:
    res = a + b
else:
    res = a * b

c = res
print(f'{c=}')