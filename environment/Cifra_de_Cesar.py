def cifra_cesar(mensagem, chave, alfabeto):
    mensagem_criptografada = ""
    
    for letra in mensagem:
        # Verifica se a letra está no alfabeto
        if letra in alfabeto:
            # Encontra a posição da letra no alfabeto
            posicao_atual = alfabeto.index(letra)
            # Calcula a nova posição considerando a chave
            nova_posicao = (posicao_atual + chave) % len(alfabeto)
            # Adiciona a letra criptografada
            mensagem_criptografada += alfabeto[nova_posicao]
        else:
            # Se não for uma letra do alfabeto, apenas adiciona a letra original
            mensagem_criptografada += letra
    
    return mensagem_criptografada

# Exemplo de uso
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
mensagem = input("Digite a mensagem: ").lower()  # Convertendo para minúsculas para simplificar
chave = int(input("Digite a chave de cifra (número): "))

mensagem_criptografada = cifra_cesar(mensagem, chave, alfabeto)
print(f'Mensagem criptografada: {mensagem_criptografada}')
