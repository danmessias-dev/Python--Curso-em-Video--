# ==========================================================
# Exercício: Seno, Cosseno e Tangente
#
# Objetivo:
# Ler um ângulo em graus e calcular o seno,
# cosseno e tangente utilizando a biblioteca math.
# ==========================================================

import math

# Entrada de dados
angulo = float(input("Informe um ângulo em graus: "))

# Converte o ângulo de graus para radianos
angulo_rad = math.radians(angulo)

# Calcula as funções trigonométricas
seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

# Saída de dados
print(f"\nÂngulo: {angulo:.1f}°")
print(f"Seno: {seno:.4f}")
print(f"Cosseno: {cosseno:.4f}")
print(f"Tangente: {tangente:.4f}")