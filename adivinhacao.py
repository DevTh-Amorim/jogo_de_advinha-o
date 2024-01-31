import random

print ("*******************************")
print ("Bem vindo no jogo de Advinhação")
print ("*******************************")

numero_secreto = random.randrange (1 , 101)
total_de_tentativas = 0
pontos = 1000

print ("Qual nivel de dificuldade voce quer?")
print ("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Define um nivel: "))
if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range (1,total_de_tentativas + 1):
    print ("Tentativa {} de {}".format(rodada,total_de_tentativas))
    chute_str = input("Digite um número de 1 a 100: ")
    print ("Voçê digitou " , chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Voçê deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print ("Voçê acertou e fez {} pontos!".format(pontos))
        break
    else:
        if (maior):
            print ("Voçê errou! O seu numero foi maior.")
        elif (menor):
            print ("Voçê errou! O seu numero foi menor.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("Fim do jogo!")