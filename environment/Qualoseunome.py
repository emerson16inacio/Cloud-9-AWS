myString = "Essa é minha string"
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString

print(myString)
print(type(myString))
print(myString + " é uma forma de data " + str(type(myString)))
print(thirdString)
print("")

nome = input("Qual é o seu nome? ")
print("Olá " + nome)
print("")

cor = input("Qual é sua cor favorita? ")
animal = input("Qual é o seu animal favorito? ")
print("{}, você gosta de {} {} !".format(nome,animal,cor))