from transacao import Transacao
from categoria import Categoria

lista_categorias = []
lista_transacoes = []


def cadastrar_categoria(nome):
    nova_categoria = Categoria(nome)
    lista_categorias.append(nova_categoria)
    return nova_categoria


def cadastrar_transacao(descricao, valor, categoria):
    nova_transacao = Transacao(descricao, valor, categoria)
    lista_transacoes.append(nova_transacao)
    return nova_transacao


def saldo_total():
    total = 0
    for t in lista_transacoes:
        total += t.valor

    return total
