# ==========================================================
# Exercício: Sorteando um aluno
#
# Objetivo:
# Ler o nome de quatro alunos e sortear um deles
# para apagar o quadro.
# ==========================================================

import random

# Entrada de dados
primeiro_aluno = input("Digite o nome do primeiro aluno: ")
segundo_aluno = input("Digite o nome do segundo aluno: ")
terceiro_aluno = input("Digite o nome do terceiro aluno: ")
quarto_aluno = input("Digite o nome do quarto aluno: ")

# Lista de alunos
alunos = [
    primeiro_aluno,
    segundo_aluno,
    terceiro_aluno,
    quarto_aluno
]

# Sorteio
aluno_escolhido = random.choice(alunos)

print(f"\nO aluno escolhido para apagar o quadro foi: {aluno_escolhido}.")