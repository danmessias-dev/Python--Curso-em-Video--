# ============================================
# Curso de Python - Exercícios da Aula 01
# Objetivo: Praticar entrada de dados (input),
# variáveis, tipos de dados e saída com f-string.
# ============================================

# --------------------------------------------
# Exercício 1 - Saudação personalizada
# Solicita o nome do usuário e exibe uma
# mensagem de boas-vindas.
# --------------------------------------------

# nome = input("Qual é seu nome? ")
# print(f"Olá {nome}! Prazer em te conhecer!")


# --------------------------------------------
# Exercício 2 - Data de nascimento
# Solicita dia, mês e ano de nascimento
# e exibe a data informada pelo usuário.
# --------------------------------------------

# dia = int(input("Dia: "))
# mes = input("Mês: ")
# ano = int(input("Ano: "))
# print(f"Você nasceu no dia {dia} de {mes} de {ano}. Correto?")


# --------------------------------------------
# Exercício 3 - Soma de dois números
# Recebe dois números inteiros e exibe
# o resultado da soma.
# --------------------------------------------

numero = int(input("Digite um número: "))
numero1 = int(input("Digite outro número: "))

soma = numero + numero1

print(f"A soma é {soma}")