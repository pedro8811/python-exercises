import requests
import time

def calcular_tempo(fun):
    def wrapper():
        tempo_inicial = time.time()
        fun()
        tempo_final = time.time() - tempo_inicial
        print(f"Duração foi de {tempo_final:.3f}s")
    return wrapper


@calcular_tempo
def pegar_cotacao_dolar():
    link = f'https://economia.awesomeapi.com.br/last/USD-BRL'
    requisicao = requests.get(link)
    requisicao = requisicao.json()
    print(requisicao['USDBRL']['bid'])

pegar_cotacao_dolar()