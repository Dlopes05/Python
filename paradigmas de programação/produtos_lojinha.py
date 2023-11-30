class produto_estoque:

    def __init__(self, produto, nome, qtd, preco, fornecedor):

        self.produto = produto

        self.nome = nome

        self.qtd = qtd

        self.preco = preco

        self.fornecedor = fornecedor


    def print_produtos_estoque(self):
        print("PRODUTO ", self.produto)

        print("Nome:", self.nome)

        print("Quantidade:", self.qtd)

        print("Preço:", self.preco)

        print("Fornecedor:", self.fornecedor,)

        print()


produto1 = produto_estoque("1","Maçã", 50, 20, "hortifruti")

produto2 = produto_estoque("2","Pasta de Dente", 20, 7, "drogasil")

produto3 = produto_estoque("3","Desodorante", 50, 11, "Old Spice")

produto4 = produto_estoque("4","Miojo", 100, 2, "Câncer")


produtos = [produto1, produto2, produto3, produto4]


for produto_estoque in produtos:

    produto_estoque.print_produtos_estoque()