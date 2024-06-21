# 10 - Faça um algoritmo que leia três notas obtidas por um aluno, e imprima na tela a média das notas.

soma = 0
for i in range(0, 3):
    soma += int(input(f'{i + 1}º Nota: '))

media = soma / 3
print(f'{media=:.1f}') 