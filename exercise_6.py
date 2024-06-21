# 6 - Faça um algoritmo que leia um valor qualquer e imprima na tela com um reajuste de 5%.

import sys

numero = input('Número: ')
if numero:
    numero = float(numero)
else:
    sys.exit('Not a number!')

reajuste = numero + (numero * 0.05)
print(f'{numero=}, com reajuste = {reajuste}')