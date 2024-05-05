class ControleEstoque:
    def __init__(self):
        self.estoque = {
            'Coco fresco': 0,
            'Kiwi': 0,
            'Laranja': 0,
            'Limão': 0,
            'Maçã verde': 0,
            'Maracujá': 0,
            'Melancia': 0
        }

    def adicionar_estoque(self, sabor, quantidade):
        if sabor in self.estoque:
            self.estoque[sabor] += quantidade
            return True
        else:
            return False

    def remover_estoque(self, sabor, quantidade):
        if sabor in self.estoque and self.estoque[sabor] >= quantidade:
            self.estoque[sabor] -= quantidade
            return True
        else:
            return False

    def total_estoque(self):
        return sum(self.estoque.values())

# Exemplo de uso:
controle = ControleEstoque()

# Adicionando 10 unidades de Kiwi ao estoque
controle.adicionar_estoque('Kiwi', 10)

# Removendo 5 unidades de Laranja do estoque
controle.remover_estoque('Laranja', 5)

# Imprimindo o total de gelo saborizado em estoque
print("Total em estoque:", controle.total_estoque())
print("Estoque por sabor:", controle.estoque)
