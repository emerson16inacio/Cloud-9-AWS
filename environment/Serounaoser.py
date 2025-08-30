import csv
import copy

# Nome do arquivo CSV
csv_filename = "frota_de_carros.csv"

# Variável para armazenar o carro encontrado
carro_encontrado = None

with open(csv_filename, mode='r', newline='', encoding='utf-8') as file:
    # Use DictReader para ler cada linha como um dicionário
    csv_reader = csv.DictReader(file)

# Itera sobre cada linha do arquivo
    for row in csv_reader:
        # Verifica se o valor da coluna 'vin' é 'TM320163'
        if row['vin'] == 'TM320163':
            # Se encontrou, armazena a linha e sai do loop
            carro_encontrado = row
            break # Importante para parar de procurar depois de encontrar

# Exibe o resultado do carro pesquisado
if carro_encontrado:
    print("Carro encontrado com sucesso:")
    for key, value in carro_encontrado.items():
        print(f"{key}: {value}")
else:
    print("Nenhum carro com o VIN 'TM320163' foi encontrado.")


# aplicação de um novo veiculo
meusVeiculos = {
    "vin" : "<vazio>",
    "fabricacao" : "<vazio>",
    "modelo" : "<vazio>",
    "ano" : 0,
    "autonomia" : 0,
    "velocidade" : 0,
    "zeroSessenta" : 0.0,
    "quilometragem" : 0
}

print("")
# mostrar a descriçao do meu carro
for chave, valor in meusVeiculos.items():
  
    print("{}:  {}".format(chave,valor))
    
meuInventario = []