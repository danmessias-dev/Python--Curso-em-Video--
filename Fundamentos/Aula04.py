# ==========================================================
# Módulos em Python
# Exemplos de utilização das bibliotecas:
# - math   -> Operações matemáticas
# - random -> Geração de números aleatórios
# - emoji  -> Exibição de emojis no terminal
# ==========================================================

# ----------------------------------------------------------
# Biblioteca math
# ----------------------------------------------------------

"""
import math

numero = int(input("Digite um número: "))

# Calcula a raiz quadrada
raiz = math.sqrt(numero)

# Arredonda para cima
print(f"A raiz quadrada de {numero} é {math.ceil(raiz)}")

# Arredonda para baixo
print(f"A raiz quadrada de {numero} é {math.floor(raiz)}")

# Exibe com duas casas decimais
print(f"A raiz quadrada de {numero} é {raiz:.2f}")
"""

# ----------------------------------------------------------
# Biblioteca random
# ----------------------------------------------------------

"""
import random

# Gera um número inteiro aleatório entre 1 e 50
numero = random.randint(1, 50)

print(numero)
"""

# ----------------------------------------------------------
# Biblioteca emoji
# Para utilizar:
# pip install emoji
# ----------------------------------------------------------

import emoji

# O parâmetro language="alias" permite utilizar nomes de emojis no formato :emoji:
print(emoji.emojize("Olá, Mundo! :earth_americas:", language="alias"))
print(emoji.emojize("Python :snake:"))
print(emoji.emojize("Foguete :rocket:"))