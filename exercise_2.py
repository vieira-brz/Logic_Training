# 2 - Faça um algoritmo para receber um número qualquer e imprimir na tela se o número é par ou ímpar, positivo ou negativo.

import sys

a = input('A: ')
if a.isdigit():
    a = float(a)
else:
    sys.exit('Not a number!')    

if a % 2 == 0:
    print(f'Par')
else:
    print('Ímpar')