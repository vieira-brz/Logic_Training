'''
12 - Faça um algoritmo que leia o valor de um produto e determine o valor que deve ser pago, conforme a escolha da forma de pagamento
pelo comprador e imprima na tela o valor final do produto a ser pago. 

Utilize os códigos da tabela de condições de pagamento para efetuar o cálculo adequado.

Tabela de Código de Condições de Pagamento
1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto
2 - À Vista no cartão de crédito, recebe 10% de desconto
3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros
4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%
'''

valor_produto = float(input('Valor produto: '))

escolha_pagamento = int(input('Escolha a forma de pagamento:\n'\
                            '1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto\n'\
                            '2 - À Vista no cartão de crédito, recebe 10% de desconto\n'\
                            '3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros\n'\
                            '4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%\n'\
                            'Forma de pagamento número: '
                        ))

valor_final = 0
if escolha_pagamento == 1:
    valor_final = valor_produto - (valor_produto * 0.15)
elif escolha_pagamento == 2:
    valor_final = valor_produto - (valor_produto * 0.10)
elif escolha_pagamento == 3:
    valor_final = valor_produto
elif escolha_pagamento == 4:
    valor_final = valor_produto + (valor_produto * 0.10)

print(f'Valor a ser pago = R${valor_final:.2f}')
