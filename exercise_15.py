'''
15 - Faça um algoritmo que leia o ano em que uma pessoa nasceu, imprima na tela quantos anos, meses e dias essa pessoa ja viveu. Leve em 
consideração o ano com 365 dias e o mês com 30 dias.
(Ex: 5 anos, 2 meses e 15 dias de vida)
'''

ano_nascimento = int(input('Ano de nascimento: '))
mes_nascimento = int(input('Mês de nascimento (1-12): '))
dia_nascimento = int(input('Dia de nascimento (1-31): '))

ano_atual = int(input('Ano atual: '))
mes_atual = int(input('Mês atual (1-12): '))
dia_atual = int(input('Dia atual (1-31): '))

anos = ano_atual - ano_nascimento

if (mes_atual < mes_nascimento) or (mes_atual == mes_nascimento and dia_atual < dia_nascimento):
    anos -= 1

if mes_atual >= mes_nascimento:
    meses = mes_atual - mes_nascimento
else:
    meses = 12 + mes_atual - mes_nascimento

if dia_atual >= dia_nascimento:
    dias = dia_atual - dia_nascimento
else:
    dias = 30 + dia_atual - dia_nascimento
    if meses == 0:
        meses = 11
        anos -= 1
    else:
        meses -= 1

print(f'{anos} anos, {meses} meses, {dias} dias de vida.')