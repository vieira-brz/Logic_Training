'''
9 - Faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma pessoa, leia o seu peso e sua altura e imprima na tela sua condição 
de acordo com a tabela abaixo:

Fórmula do IMC = peso / (altura) ²

Tabela Condições IMC:
Abaixo de 18,5   | Abaixo do peso          
Entre 18,6 e 24,9 | Peso ideal (parabéns)  
Entre 25,0 e 29,9 | Levemente acima do peso
Entre 30,0 e 34,9 | Obesidade grau I 
Entre 35,0 e 39,9 | Obesidade grau II (severa)
Maior ou igual a 40 | Obesidade grau III (mórbida)
'''

import sys

def imc(peso, altura):
    return peso / (altura ** 2)

def condicao(imc):
    if imc < 18.5:
        return 'abaixo do peso'
    elif imc > 18.5 and imc < 24.9:
        return 'peso ideal (parabéns)'
    elif imc > 25 and imc < 29.9:
        return 'levemente acima do peso'
    elif imc > 30 and imc < 34.9:
        return 'obesidade gray I'
    elif imc > 35 and imc < 39.9:
        return 'obesidade gray II (severa)'
    else:
        return 'obesidade grau III (mórbida)'

peso = input('Peso (kg): ')
if peso.isdigit():
    peso = int(peso)
else:
    sys.exit('Not a valid number!')

altura = input('Altura (m, ex: 1.75): ')
if altura:
    altura = float(altura)
else:
    sys.exit('Not a valid number!')

my_imc = imc(peso, altura)
print(f'Sua condição é {condicao(my_imc)}, IMC = {my_imc}!') 