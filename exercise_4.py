# 4 - Faça um algoritmo que receba um número inteiro e imprima na tela o seu antecessor e o seu sucessor.

import sys

a = input('A: ')
if a.isdigit():
    a = int(a)
else:
    sys.exit('Not a integer!')    

print(f'{a=}, antecessor = {a - 1}, sucessor = {a + 1}')