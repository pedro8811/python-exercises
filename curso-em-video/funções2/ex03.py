jogador = str(input("Nome do Jogador: ")).strip()
gols = str(input("Número de Gols: ")).strip()
def ficha(nome=None, gols=None):
    if nome != '':
        print(f"O jogador {nome} ", end="")
    else:
        print(f'O jogador <desconhecido> ', end="")

    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0

    print(f"fez {gols} gol(s) no campeonato.")

ficha(jogador, gols)