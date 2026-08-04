# ==========================================================
# Exercício: Sorteando a ordem de apresentação
#
# Objetivo:
# Ler o nome de quatro alunos e exibir uma ordem
# aleatória para a apresentação dos trabalhos.
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

# Embaralha a ordem da lista
random.shuffle(alunos)

# Exibe a ordem sorteada
print("\nOrdem de apresentação:")

for aluno in alunos:
    print(aluno)