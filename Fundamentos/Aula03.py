# Operadores Aritméticos em Python

# Este exemplo apresenta os principais operadores aritméticos da linguagem Python e suas aplicações em operações matemáticas.

## Operadores
'''
| Operador | Descrição | Exemplo |
|----------|-----------|---------|
| `+` | Adição | `5 + 3` |
| `-` | Subtração | `5 - 3` |
| `*` | Multiplicação | `5 * 3` |
| `/` | Divisão | `10 / 2` |
| `//` | Divisão inteira | `10 // 3` |
| `%` | Resto da divisão (módulo) | `10 % 3` |
| `**` | Potenciação | `2 ** 3` |
'''
## Exemplo

# python
# Exemplo de utilização dos operadores aritméticos.

a = 10
b = 3

print(f"Adição: {a} + {b} = {a + b}")
print(f"Subtração: {a} - {b} = {a - b}")
print(f"Multiplicação: {a} * {b} = {a * b}")
print(f"Divisão: {a} / {b} = {a / b}")
print(f"Divisão inteira: {a} // {b} = {a // b}")
print(f"Resto da divisão: {a} % {b} = {a % b}")
print(f"Potenciação: {a} ** {b} = {a ** b}")

## O que aprendi
'''
- Utilizar os operadores aritméticos do Python.
- Entender a diferença entre divisão (`/`) e divisão inteira (`//`).
- Utilizar o operador `%` para obter o resto de uma divisão.
- Realizar cálculos de potência com `**`.
'''

## Exemplos de aplicação

### Verificar se um número é par
'''
python
numero = 8
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
'''

### Calcular a área de um retângulo
'''
python
largura = 5
altura = 8

area = largura * altura

print(f"Área do retângulo: {area}")
'''

### Calcular uma potência
'''
python
base = 4
expoente = 2

resultado = base ** expoente

print(f"{base} elevado a {expoente} é igual a {resultado}")
'''