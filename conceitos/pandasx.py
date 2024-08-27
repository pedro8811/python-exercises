import pandas as pd
import openpyxl

# dataframe
tabela_clientes = pd.read_csv("clientes.csv")
# print(tabela_clientes)

dicionario_produtos = {"nome": ["iphone", "ipad", "airpod"], "preco": [5000, 9000, 2000], "estoque": [100, 50, 60]}

tabela_produtos = pd.DataFrame(dicionario_produtos)
print(tabela_produtos)

lista_produtos = [
    {"nome": "iphone", "preco": 5000, "estoque": 100},
    {"nome": "ipad", "preco": 9000, "estoque": 50},
    {"nome": "airpod", "preco": 2000, "estoque": 60}
]
