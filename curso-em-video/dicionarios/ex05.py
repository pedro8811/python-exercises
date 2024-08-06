jogadores = list()
jogador = dict()
option = 's'
while option == 's':
    jogador["nome"] = str(input("Digite o nome do jogador: "))
    jogador["partidas"] = int(input("Quantidade de partidas jogadas: "))
    jogador["golsporpartida"] = []
    jogador["mediagols"] = 0
    jogador["totalgols"] = 0
    for x in range(0, jogador["partidas"]):
        jogador["golsporpartida"].append(int(input(f"Quantos gols na partida {x}: ")))

    for x in jogador["golsporpartida"]:
        jogador["totalgols"] += x

    jogador["mediagols"] = jogador["totalgols"] / jogador["partidas"]

    jogadores.append(jogador.copy())
    option = str(input("Deseja adicionar mais um jogador? [s/n] ")).strip().lower()

print()

print("=-"*20)
print('cod  nome             gols         total')
print('-'*40)
cod = 0
for x in jogadores:
    print(f'{cod}  {x["nome"]}             {x["golsporpartida"]}         {x["totalgols"]}')
    cod += 1
print("-=" * 20)
