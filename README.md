# 📘 Lista de Exercícios Python - EDN

# Exercício 1: Apresente-se!
```
print("=== Exercício 1: Apresente-se! ===")

nome = "Ana"
idade = 25
cidade = "São Paulo"

print("Seu nome é {}, você tem {} e você mora na cidade {}.".format(nome, idade, cidade))  

print()
```
# Exercício 2: Média de uma lista

```
print("=== Exercício 2: Média de uma lista ===")

numeros = [10, 20, 30, 40, 50]

media = sum(numeros) / len(numeros)
print("A média dos números é: {}".format(media))
print()

````
# Exercício 3: Quem gastou mais dinheiro?

```
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

```
# Exercício 4: Maior e menor palavra

```
print("=== Exercício 4: Maior e menor palavra ===")

palavras = ["python", "asimov", "código", "web", "programação"]

maior_palavra = palavras[0]
menor_palavra = palavras[0]

for palavra in palavras:
    if len(palavra) > len(maior_palavra):
        maior_palavra = palavra
    if len(palavra) < len(menor_palavra):
        menor_palavra = palavra

print("A maior palavra é:", maior_palavra)
print("A menor palavra é:", menor_palavra)
print("")

```
# Exercício 5: Segundo maior valor

````
print("=== Exercício 5: Segundo maior valor ===")

numeros = [32, 10, 58, 30, 55, 12, 28, 51]

numeros_unicos = list(set(numeros)) 
numeros_ordenados = sorted(numeros_unicos, reverse=True)
segundo_maior = numeros_ordenados[1]

print("O segundo maior valor é: {segundo_maior}")
print()

````
