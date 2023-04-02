import random

def jogar():
    imprimir_mensagem_abertura()
    nome_arquivo = selecionando_biblioteca()
    palavra_secreta = sorteio_palavra_secreta(nome_arquivo)
    letras_acertadas = inicializacao_letras_acertadas(palavra_secreta)

    print("A palavra a seguir é:")
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        chute = recebe_chute_jogador()

        if(chute in palavra_secreta):
            analisa_chute(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print("__________________________________")
        print(letras_acertadas)

    print("__________________________________")

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    print("Fim de jogo.")

def imprimir_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

def selecionando_biblioteca():
    print("Bibliotecas de palavras disponíveis, digite o número desejado:")
    print("1 - Frutas   2 - Nomes")
    opcao = input("selecione uma opção:")
    nome_arquivo = ""

    if(opcao == "1"):
        nome_arquivo = "frutas.txt"
    elif(opcao == "2"):
        nome_arquivo = "nomes.txt"
    return nome_arquivo

def sorteio_palavra_secreta(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializacao_letras_acertadas(palavra_secreta):
    return ['_' for letra in palavra_secreta]

def recebe_chute_jogador():
    chute = input("Digite uma letra:")
    chute = chute.strip().upper()
    return chute

def analisa_chute(chute, palavra_secreta, letras_acertadas):
    posicao = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[posicao] = letra
        posicao += 1

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")

if(__name__ == "__main__"):
    jogar()













