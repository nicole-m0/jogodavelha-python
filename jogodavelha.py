# mudando algumas cores do código com a biblioteca colorama
from colorama import Fore

def interface():
    print("   0   1   2")
    print("0 [{}] [{}] [{}]".format(tabuleiro[0][0], tabuleiro[0][1], tabuleiro[0][2]))
    print("1 [{}] [{}] [{}]".format(tabuleiro[1][0], tabuleiro[1][1], tabuleiro[1][2]))
    print("2 [{}] [{}] [{}]".format(tabuleiro[2][0], tabuleiro[2][1], tabuleiro[2][2]))

def validarVitoria(rodada):
    global parar
    # HORIZONTAL ---------------------------------------------------------------------------
    if(tabuleiro[0][0] == rodada and tabuleiro[0][1] == rodada and tabuleiro[0][2] == rodada):
        interface()
        print(Fore.GREEN + "O {} Venceu!".format(rodada))
        parar = True

    if (tabuleiro[1][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro[1][2] == rodada):
            interface()
            print(Fore.GREEN + "O {} Venceu!".format(rodada))
            parar = True

    if (tabuleiro[2][0] == rodada and tabuleiro[2][1] == rodada and tabuleiro[2][2] == rodada):
                interface()
                print(Fore.GREEN + "O {} Venceu!".format(rodada))
                parar = True

    # VERTICAL ------------------------------------------------------------------------------
    if (tabuleiro[0][0] == rodada and tabuleiro[1][0] == rodada and tabuleiro[2][0] == rodada):
        interface()
        print(Fore.GREEN + "O {} Venceu!".format(rodada))
        parar = True

    if (tabuleiro[0][1] == rodada and tabuleiro[1][1] == rodada and tabuleiro[2][1] == rodada):
        interface()
        print(Fore.GREEN + "O {} Venceu!".format(rodada))
        parar = True

    if (tabuleiro[0][2] == rodada and tabuleiro[1][2] == rodada and tabuleiro[2][2] == rodada):
        interface()
        print(Fore.GREEN + "O {} Venceu!".format(rodada))
        parar = True

# DIAGONAIS ----------------------------------------------------------------------------------
    if(tabuleiro[0][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro[2][2] == rodada):
            interface()
            print(Fore.GREEN + "O {} Venceu!".format(rodada))
            parar = True

    if (tabuleiro[2][0] == rodada and tabuleiro[1][1] == rodada and tabuleiro[0][2] == rodada):
        interface()
        print(Fore.GREEN + "O {} Venceu!".format(rodada))
        parar = True


tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

parar = False
rodada = "x"
jogadas = 0

while parar == False:
    if jogadas == 9:
        interface()
        print(Fore.YELLOW + "Empate!")
        parar = True

    interface()

    linha = int(input(Fore.CYAN + "Digite a linha escolhida: "))
    coluna = int(input(Fore.CYAN + "Digite a coluna escolhida: "))

    if rodada == "x":
        tabuleiro[linha][coluna] = "x"
        validarVitoria(rodada)
        jogadas += 1
        rodada = "o"

    elif rodada == "o":
        tabuleiro[linha][coluna] = "o"
        validarVitoria(rodada)
        jogadas += 1
        rodada = "x"

# testando opção de reiniciar o jogo
def reiniciar():
    continuar = "y"
    while continuar:
        continuar = str(input("Deseja iniciar mais uma partida? y/n"))
        if continuar:
            interface()
        else: print(Fore.LIGHTWHITE_EX + "Jogo Encerrado!")


