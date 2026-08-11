class Produto:
    def __init__(self, nome: str, preco: float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def reduzir_estoque(self, quantidade):
        if self.estoque - quantidade >= 0:
            self.estoque -= quantidade
        else:
            print("Estoque insuficiente!")


class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_ao_carrinho(self, produto, quantidade):
        self.produtos.append((produto, quantidade))

    def mostrar_carrinho(self):
        for produto, quantidade in self.produtos:
            print(f"Produto: {produto.nome}")
            print(f"Quantidade: {quantidade}")
            print(f"Preço: R$ {produto.preco}")
            print(f"Subtotal: R$ {produto.preco * quantidade}")
            print()


def main():
    arroz = Produto("Arroz", 25.50, 10)
    feijao = Produto("Feijão", 8.50, 20)

    carrinho = CarrinhoDeCompras()

    carrinho.adicionar_ao_carrinho(arroz, 2)
    carrinho.adicionar_ao_carrinho(feijao, 3)

    carrinho.mostrar_carrinho()


if __name__ == "__main__":
    main()