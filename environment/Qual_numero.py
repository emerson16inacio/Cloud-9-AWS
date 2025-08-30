import random

numero = random.randint(1,10)
issoEstaCerto = False

while issoEstaCerto != True:
    escolha = input("Escolha um número de 1 a 10: ")
    if int(escolha) == numero:
        print("Você escolheu {}. Está corretissimo! Você ganhou".format(escolha))
        issoEstaCerto = True
    else:
        print("Você escolheu {}. Está Erradissimo! Você Perdeu".format(escolha))

       
print("")
for x in range (0, 11):
    print(x)

