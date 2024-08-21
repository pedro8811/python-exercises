from utilitarios import *


# categorias
categoria_receitas = cadastrar_categoria("Receitas")
categoria_lazer = cadastrar_categoria("Lazer")
categoria_contas = cadastrar_categoria("Contas Fixas")
categoria_viagens = cadastrar_categoria("Viagens")

cadastrar_transacao('Salário Ago/2024', 1000, categoria_receitas)
cadastrar_transacao('Bonus', 50, categoria_receitas)

cadastrar_transacao('Ingresso Show', -150, categoria_lazer)
cadastrar_transacao('Energia', -100, categoria_contas)

cadastrar_transacao('Disney', -400, categoria_viagens)

total = saldo_total()
print(f'Saldo total: {total}')
