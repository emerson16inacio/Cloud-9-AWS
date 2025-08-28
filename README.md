# 📘 Lista de Exercícios Python - EDN
# Autor: Emerson Inácio

# --------------------------------------------
# Exercício 1: Apresente-se!
print("=== Exercício 1: Apresente-se! ===")
nome = "Ana"
idade = 25
cidade = "São Paulo"
print(f"Olá, meu nome é {nome}, tenho {idade} anos e moro em {cidade}.")
print()

# --------------------------------------------
# Exercício 2: Média de uma lista
print("=== Exercício 2: Média de uma lista ===")
numeros = [10, 20, 30, 40, 50]
media = sum(numeros) / len(numeros)
print(f"A média é: {media}")
print()

# --------------------------------------------
# Exercício 3: Quem gastou mais dinheiro?
print("=== Exercício 3: Quem gastou mais dinheiro? ===")
gastos_joao = [300, 500, 200, 800]
gastos_pedro = [200, 400, 500, 700]

total_joao = sum(gastos_joao)
total_pedro = sum(gastos_pedro)

if total_joao > total_pedro:
    print(f"João gastou mais: {total_joao}")
elif total_pedro > total_joao:
    print(f"Pedro gastou mais: {total_pedro}")
else:
    print("Os dois gastaram o mesmo valor.")
print()

# --------------------------------------------
# Exercício 4: Maior e menor palavra
print("=== Exercício 4: Maior e menor palavra ===")
palavras = ["python", "asimov", "código", "web", "programação"]

maior = max(palavras, key=len)
menor = min(palavras, key=len)

print(f"A maior palavra é: {maior}")
print(f"A menor palavra é: {menor}")
print()

# --------------------------------------------
# Exercício 5: Segundo maior valor
print("=== Exercício 5: Segundo maior valor ===")
numeros = [32, 10, 58, 30, 55, 12, 28, 51]

numeros_unicos = list(set(numeros))  # remove duplicados
numeros_ordenados = sorted(numeros_unicos, reverse=True)
segundo_maior = numeros_ordenados[1]

print(f"O segundo maior valor é: {segundo_maior}")
print()

print("✅ Todos os exercícios foram executados com sucesso!")
