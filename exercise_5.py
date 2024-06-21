'''
5 - Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de um usuário, calcule quantos salários mínimos esse 
usuário ganha e imprima na tela o resultado. (Base para o Salário mínimo R$ 1.293,20).
'''

import sys

minimo = 1293.20
usuario = input('Seu salário (exemplo: 1293.20): ')

if usuario:
    usuario = float(usuario)

    if usuario < minimo:
        sys.exit('Salário informado menor que o mínimo!')
else:
    sys.exit('Not a number!')


res = usuario / minimo

print(f'Você recebe {res:.1f}x um salário mínimo de R${minimo}!')