import random
import sys


vazio = " "

jogo_posicao_vitoria = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", vazio]
]

jogo_posicao = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", vazio]
]


def menu():
    print("""
╔══════════════════════════════════════════════╗
║  O jogo termina quando você conseguir        ║
║  colocar no formato abaixo:                  ║
║                                              ║
║              ┌───┬───┬───┐                  ║
║              │ 1 │ 2 │ 3 │                  ║
║              ├───┼───┼───┤                  ║
║              │ 4 │ 5 │ 6 │                  ║
║              ├───┼───┼───┤                  ║
║              │ 7 │ 8 │   │                  ║
║              └───┴───┴───┘                  ║
║                                              ║
║  Use as teclas W, A, S, D para mover         ║
║  o espaço em branco.                         ║
╚══════════════════════════════════════════════╝
""")

    input("Pressione Enter para começar...")

    embaralha(jogo_posicao)

    while jogo_posicao != jogo_posicao_vitoria:

        print(tela(jogo_posicao))

        linha, coluna = posicao_vazio(jogo_posicao)

        movimento = move_vazio((linha, coluna))

        move_direcao(jogo_posicao, movimento, linha, coluna)

    print(tela(jogo_posicao))
    print("Parabéns! Você ganhou!!!")


def movimentos_validos(linha, coluna):
    movimentos = []

    if linha > 0:
        movimentos.append("W")

    if coluna > 0:
        movimentos.append("A")

    if linha < 2:
        movimentos.append("S")

    if coluna < 2:
        movimentos.append("D")

    return movimentos


def move_direcao(posicao, movimento, linha, coluna):

    if movimento == "W":
        posicao[linha][coluna], posicao[linha - 1][coluna] = \
            posicao[linha - 1][coluna], posicao[linha][coluna]

    elif movimento == "A":
        posicao[linha][coluna], posicao[linha][coluna - 1] = \
            posicao[linha][coluna - 1], posicao[linha][coluna]

    elif movimento == "S":
        posicao[linha][coluna], posicao[linha + 1][coluna] = \
            posicao[linha + 1][coluna], posicao[linha][coluna]

    elif movimento == "D":
        posicao[linha][coluna], posicao[linha][coluna + 1] = \
            posicao[linha][coluna + 1], posicao[linha][coluna]


def move_vazio(posicao_vazio):
    linha, coluna = posicao_vazio

    movimentos = movimentos_validos(linha, coluna)

    print("""
╔════════════════════════════════════════════════════╗
║ Digite W, A, S, D para mover e SAIR para sair...  ║
╚════════════════════════════════════════════════════╝
""")

    movimento = ""

    while movimento not in movimentos and movimento != "SAIR":

        movimento = input("> ").upper()

        if movimento not in movimentos and movimento != "SAIR":
            print("Movimento inválido! Tente novamente.")

    if movimento == "SAIR":
        print("Até mais!")
        sys.exit()

    return movimento


def posicao_vazio(posicao):
    for i in range(len(posicao)):
        for j in range(len(posicao[i])):

            if posicao[i][j] == vazio:
                return i, j


def tela(posicao):
    posicoes = []

    for linha in posicao:
        for coluna in linha:
            posicoes.append(coluna)

    return """
╔════════════════════════════════════════════════════╗
║                    NUMPUZ                          ║
╚════════════════════════════════════════════════════╝
╔════════════════════════════════════════════════════╗
║                                                    ║
║                   ╔═════════════╗                  ║
║                   ║ {} | {} | {} ║                  ║
║                   ║─────────────║                  ║
║                   ║ {} | {} | {} ║                  ║
║                   ║─────────────║                  ║
║                   ║ {} | {} | {} ║                  ║
║                   ╚═════════════╝                  ║
║                                                    ║
╚════════════════════════════════════════════════════╝
""".format(*posicoes)


def embaralha(posicao):
    for i in range(100):

        linha, coluna = posicao_vazio(posicao)

        movimentos = movimentos_validos(linha, coluna)

        movimento = random.choice(movimentos)

        move_direcao(posicao, movimento, linha, coluna)


menu()