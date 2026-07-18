'''
Operadores Aritméticos em Python

Os operadores aritméticos são utilizados para realizar cálculos matemáticos.

| Operador | Descrição                 |  Exemplo  | Resultado |
| :------: | ------------------------- | :-------: | :-------: |
|    `+`   | Adição                    |  `5 + 3`  |    `8`    |
|    `-`   | Subtração                 |  `5 - 3`  |    `2`    |
|    `*`   | Multiplicação             |  `5 * 3`  |    `15`   |
|    `/`   | Divisão                   |  `10 / 2` |   `5.0`   |
|   `//`   | Divisão Inteira           | `10 // 3` |    `3`    |
|    `%`   | Resto da Divisão (Módulo) |  `10 % 3` |    `1`    |
|   `**`   | Potenciação               |  `2 ** 3` |    `8`    |

---

# Exemplo de Código

```python
# Declarando duas variáveis
a = 10
b = 3

# Operações aritméticas
print(f"Adição: {a} + {b} = {a + b}")
print(f"Subtração: {a} - {b} = {a - b}")
print(f"Multiplicação: {a} * {b} = {a * b}")
print(f"Divisão: {a} / {b} = {a / b}")
print(f"Divisão Inteira: {a} // {b} = {a // b}")
print(f"Resto da Divisão: {a} % {b} = {a % b}")
print(f"Potenciação: {a} ** {b} = {a ** b}")
```

### Saída

```text
Adição: 10 + 3 = 13
Subtração: 10 - 3 = 7
Multiplicação: 10 * 3 = 30
Divisão: 10 / 3 = 3.3333333333333335
Divisão Inteira: 10 // 3 = 3
Resto da Divisão: 10 % 3 = 1
Potenciação: 10 ** 3 = 1000
```

---

# Observações

* `/` → Sempre retorna um valor do tipo `float`.
* `//` → Retorna apenas a parte inteira da divisão.
* `%` → Retorna o resto da divisão.
* `**` → Calcula a potência de um número.

---

# Exemplos Práticos

## Verificando se um número é par

```python
numero = 8

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
```

---

## Calculando a área de um retângulo

```python
largura = 5
altura = 8

area = largura * altura

print(f"Área do retângulo: {area}")
```

---

## Calculando uma potência

```python
base = 4
expoente = 2

resultado = base ** expoente

print(f"{base} elevado a {expoente} é igual a {resultado}")
'''

