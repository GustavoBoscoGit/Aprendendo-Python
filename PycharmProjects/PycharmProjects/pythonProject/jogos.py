import adivinhacao
import forca

print("(1) Jogo Adivinhacao (2) Jogo Forca")
op = int(input("Escolha o jogo: "))

if(op == 1):
    adivinhacao.jogar()
elif(op == 2):
    forca.jogar()

