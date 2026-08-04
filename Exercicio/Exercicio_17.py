# ==========================================================
# Exercício: Calculando a Hipotenusa
#
# Objetivo:
# Ler os comprimentos dos catetos de um triângulo retângulo
# e calcular o comprimento da hipotenusa utilizando a
# biblioteca math.
# ==========================================================

import math

# Entrada de dados
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

# ----------------------------------------------------------
# Opção 1: Utilizando a fórmula de Pitágoras
# hipotenusa = math.sqrt((cateto_oposto ** 2) + (cateto_adjacente ** 2))
# ----------------------------------------------------------

# Opção 2: Utilizando a função math.hypot()
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

# Saída de dados
print(f"\nO comprimento da hipotenusa é {hipotenusa:.2f}.")