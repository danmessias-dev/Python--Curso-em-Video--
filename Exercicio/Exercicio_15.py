# ==========================================================
# Exercício: Aluguel de Carros
#
# Objetivo:
# Calcular o valor a ser pago pelo aluguel de um carro.
#
# Regras:
# - R$ 60,00 por dia alugado.
# - R$ 0,15 por quilômetro percorrido.
# ==========================================================

# Entrada de dados
dias_alugados = int(input("Quantidade de dias alugados: "))
quilometros_percorridos = float(input("Quilômetros percorridos: "))

# Cálculo do valor total
valor_total = (dias_alugados * 60) + (quilometros_percorridos * 0.15)

# Saída de dados
print(f"\nO total a pagar é R$ {valor_total:.2f}")