import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    numero_de_tentativas = 0
    pontos = 1000

    print("Níveis de dificuldade:")
    print("1 - Fácil    2 - Médio   3 - Difícil")

    nivel = int(input("Selecione o nível de dificuldade:"))
    if(nivel == 1):
        numero_de_tentativas = 20
    elif(nivel == 2):
        numero_de_tentativas = 10
    else:
        numero_de_tentativas = 5
    print("___________________________________")

    for rodada in range(1, numero_de_tentativas + 1):
        print("tentativa {} de {}".format(rodada, numero_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            print("_________________________________________________________")
            continue

        acertou   = chute == numero_secreto
        maior_que = chute > numero_secreto
        menor_que = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if(maior_que):
                print("Você errou! O seu chute foi maior do que o número secreto.")
                if(rodada == numero_de_tentativas):
                    print("O número secreto era {}. Você fez um total de {} pontos.".format(numero_secreto, pontos))
            elif(menor_que):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                if(rodada == numero_de_tentativas):
                    print("O número secreto era {}. Você fez um total de {} pontos.".format(numero_secreto, pontos))
        print("_________________________________________________________")

    print("Fim de jogo.")

if(__name__ == "__main__"):
    jogar()












