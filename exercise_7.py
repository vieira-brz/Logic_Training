# 7 - Faça um algoritmo que leia dois valores booleanos (lógicos) e determine se ambos são VERDADEIRO ou FALSO.

def ler_valor_booleano(mensagem):
    while True:
        valor = input(mensagem + " (True/False): ")
        if valor.lower() in ['true', 'false']:
            return valor.lower() == 'true'
        else:
            print("Entrada inválida. Por favor, insira 'True' ou 'False'.")

valor1 = ler_valor_booleano("Digite o primeiro valor booleano")
valor2 = ler_valor_booleano("Digite o segundo valor booleano")

if valor1 and valor2:
    resultado = "Ambos os valores são VERDADEIRO."
elif not valor1 and not valor2:
    resultado = "Ambos os valores são FALSO."
else:
    resultado = "Os valores são diferentes."

print(resultado)