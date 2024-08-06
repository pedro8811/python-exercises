# MINHA SOLUÇÃO
from random import randint
from time import sleep
from operator import itemgetter
# pessoas = []
# numbers = [randint(1, 6), randint(1, 6), randint(1, 6)]
# numbers.sort(reverse=True)
# pessoa = {}
# for x in range(0, 3):
#     pessoa['nome'] = str(input("Digite o nome: "))
#     pessoa['numero'] = numbers[x]
#     # print(f'O {pessoa["nome"]} tirou o número {pessoa["numero"]}')
#     pessoas.append(pessoa.copy())
# counter = 1
# for pos, x in enumerate(pessoas):
#     print(f'{pos+1}° lugar: {x["nome"]} com {x["numero"]}')

# SOLUÇÃO DO VIDEO
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = dict()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f"{i}° lugar: {v[0]} com {v[1]}.")
    sleep(.5)