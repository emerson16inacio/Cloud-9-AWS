nome = "Ana" 
idade = 25 
cidade = "São Paulo" 
numeros = [10, 20, 30, 40, 50]  

# sum calcula a soma dos elementos da lista
# len calcula a quantidade de elementos da lista
media = sum(numeros) / len(numeros)
 
print("Seu nome é {}, você tem {} e você mora na cidade {}.".format(nome, idade, cidade))  
print("")
print("A média dos números é: {}".format(media))

#pode fazer desta forma tambem

#soma = 0
#contador = 0
#for numero in numeros:
#    soma += numero  # Adiciona o número atual à soma
#    contador += 1   # Incrementa o contador
#media = soma / contador  # Calcula a média
#print("A média é:", media)

gastos_joao = [300, 500, 200, 800]
gastos_pedro = [200, 400, 500, 700]

total_joao = sum(gastos_joao)
total_pedro = sum(gastos_pedro)

if total_joao > total_pedro:
    print("João gastou mais: R${}".format(total_joao))
elif total_pedro > total_joao:
    print("Pedro gastou mais: R${}".format(total_pedro))
else:
    print("Ambos gastaram a mesma quantia: R${}".format(total_joao))
    
print("")

palavras = ["python", "asimov", "código", "web", "programação"]

# Inicializando as variáveis para a maior e a menor palavra
maior_palavra = palavras[0]
menor_palavra = palavras[0]
# Loop para percorrer a lista de palavras
for palavra in palavras:
    # Verifica se a palavra atual é maior que a maior_palavra
    if len(palavra) > len(maior_palavra):
        maior_palavra = palavra
    # Verifica se a palavra atual é menor que a menor_palavra
    if len(palavra) < len(menor_palavra):
        menor_palavra = palavra
# Exibindo os resultados
print("A maior palavra é:", maior_palavra)
print("A menor palavra é:", menor_palavra)
print("")

numeros = [32, 10, 58, 30, 55, 12, 28, 51]
# Remover duplicatas e ordenar a lista em ordem decrescente
numeros_unicos = list(set(numeros))  # Remove duplicatas
numeros_unicos.sort(reverse=True)  # Ordena em ordem decrescente
# O segundo maior valor é o segundo elemento da lista ordenada
segundo_maior = numeros_unicos[1]
# Exibindo o resultado
print("O segundo maior valor é:", segundo_maior)