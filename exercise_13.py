# 13 - Faça algoritmo que leia o nome e a idade de uma pessoa e imprima na tela o nome da pessoa e se ela é maior ou menor de idade. 

nome = input('Nome: ')
idade = int(input('Idade: '))

maior_de_idade = 'maior de idade' if idade >= 18 else 'menor de idade'

print(f'{nome} é {maior_de_idade}')