'''
11 - Faça um algoritmo que leia quatro notas obtidas por um aluno, calcule a média das nota obtidas, imprima na tela o nome do aluno e 
se o aluno foi aprovado ou reprovado. Para o aluno ser considerado aprovado sua média final deve ser maior ou igual a 7.
'''

nome = input('Nome do aluno: ')
soma = 0
for i in range(0, 4):
    soma += int(input(f'{i + 1}º Nota: '))

media = soma / 4

resultado = 'APROVADO' if media >= 7 else 'REPROVADO'

print(f'Aluno {nome} com média {media:.1f} foi considerado {resultado}!') 