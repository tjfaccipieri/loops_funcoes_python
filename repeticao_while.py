import random

numero = random.randint(1, 10)
acertou = False

while acertou != True:
    chute = input("Chuta um numero de 1 a 10 ai meu bom: ")
    if int(chute) == numero:
        print("Acerto miseravi, o numero certo era realmente o numero {}".format(numero))
        acertou = True
    else:
        print("Você chutou o numero {}, e não passou nem perto".format(chute))


