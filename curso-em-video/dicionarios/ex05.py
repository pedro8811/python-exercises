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
print('-'*40)
cod = 1
for x in jogadores:
    print(f'{cod}  {x["nome"]}             {x["golsporpartida"]}         {x["totalgols"]}')
    cod += 1
print("=" * 40)

jogadoroption = int()
while jogadoroption != 999:
    for i, x in enumerate(jogadores):
        if i == jogadoroption - 1:
            print(f' -- LEVANTAMENTO DO JOGADOR {x["nome"]}')
            for pos, x in enumerate(x["golsporpartida"]):
                print(f'     => {pos+1}° partida fez {x} gols')
    jogadoroption = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    print('-'*40)