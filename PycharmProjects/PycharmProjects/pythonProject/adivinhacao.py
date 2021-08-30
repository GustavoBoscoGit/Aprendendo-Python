import random

def jogar():

    print("\nJogo advinhacao\n")
    numero_secreto = int(random.random() * 100)

    print("Escolha o nivel de dificuldade")
    print("(1) Facil, (2) Medio, (3) Dificil")

    nivel = int(input("Escolha o nivel:"))

    if(nivel == 1):
        tentativas = 15
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):

        print("tentativa {} de {}".format(rodada, tentativas))
        chute_str = input("Digite o seu numero: ")
        chute = int(chute_str)

        if(chute < 0):
            print("Numero invalido")
            break

        if(chute == numero_secreto):
            print("Voce acertou\n")
            break
        else:
            if(chute > numero_secreto):
                print("Seu chute foi maior que o numero secreto\n")
            elif(chute < numero_secreto):
                print("Seu chute foi menor que o numero secreto\n")

    print("Fim do Jogo!")
    print("O numero secreto era: ",numero_secreto)

if(__name__ == '__main__'):
    jogar()