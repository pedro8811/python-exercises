
class Vendedor():
    def __init__(self, nome):
        self.nome = nome

    def vendeu(self, vendas):
        self.vendas = vendas

    def bateu_meta(self, meta):
        if self.vendas >= meta:
            print(f'{self.nome} bateu a meta!')
        else:
            print(f'{self.nome} não bateu a meta.')


vendedor1 = Vendedor("Pedro")
vendedor1.vendeu(1000)
vendedor1.bateu_meta(600)

vendedor2 = Vendedor("Alon")
vendedor2.vendeu(300)
vendedor2.bateu_meta(600)
