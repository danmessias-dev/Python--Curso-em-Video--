# ==========================================================
# Exercício: Parte inteira de um número
#
# Objetivo:
# Ler um número real e exibir apenas sua parte inteira
# utilizando a biblioteca math.
# ==========================================================

import math

# Lê um número real informado pelo usuário
numero_real = float(input("Digite um número real: "))

# Obtém a parte inteira do número
parte_inteira = math.floor(numero_real)

# Exibe o resultado
print(f"O número {numero_real} tem a parte inteira {parte_inteira}.")