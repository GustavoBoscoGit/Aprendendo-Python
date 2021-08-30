import random

def jogar():

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Informe a letra: ")
        chute = chute.strip().upper()#tira os espaços da frente do texto inputado(    abc     ) fica (abc)

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        if (erros == 10):
            print("Acabaram as tentativas")
            break
        if ("_" not in letras_acertadas):
            break
        print(letras_acertadas)

    print("Fim do jogo")

if(__name__ == '__main__'):
    jogar()