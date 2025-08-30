enviarPacote = input("Você quer enviar um pacote? (Digite sim ou não e aperte Enter)")

if enviarPacote == "sim":
    print("Eu te ajudarei a enviar o pacote !")
else:
    print("Então volte quando quiser enviar um pacote. Tenha um bom dia.")
    
estampas = input("O que você quer é comprar estampas, comprar um envelope, ou fazer uma copia? (Digite estampas, envelope, ou copia) ")
if estampas == "estampas":
    print("Então quantas estampas você quer? ")
elif estampas == "envelope":
    print("Quantos envelopes você quer? ")
elif estampas == "copia":
    copias = input("Quantas compias você quer? ")
    print("Você quer {} copias.".format(copias))
else:
    print("Obrigado e volte sempre :D .")

