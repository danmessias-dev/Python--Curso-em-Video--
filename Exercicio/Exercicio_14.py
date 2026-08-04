# ==========================================================
# Exercício: Conversão de Temperatura
#
# Objetivo:
# Converter uma temperatura em graus Celsius (°C)
# para graus Fahrenheit (°F).
# ==========================================================

# Entrada de dados
temperatura_celsius = float(input("Informe a temperatura em °C: "))

# Conversão para Fahrenheit
temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32

# Saída de dados
print(
    f"A temperatura de {temperatura_celsius:.1f}°C "
    f"corresponde a {temperatura_fahrenheit:.1f}°F."
)