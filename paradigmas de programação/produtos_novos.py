class protudo_novo:

    def __init__(self, produto, nome, qtd, preco, fornecedor, prazo):

        self.produto = produto

        self.nome = nome

        self.qtd = qtd

        self.preco = preco

        self.fornecedor = fornecedor

        self.prazo = prazo

    def print_produtos_novos(self):

        print("PRODUTO", self.produto)

        print("Nome:", self.nome)

        print("Quantidade:", self.qtd)

        print("Preço:", self.preco)

        print("Fornecedor:", self.fornecedor)

        print("Prazo:", self.prazo)

        print()

produto1 = protudo_novo("1","Melância", 33, 25, "Hortifruti", "10/12/2023")

produto2 = protudo_novo("2","Chocolate", 100, 5, "Cacau Show", "03/12/2023")

produto3 = protudo_novo("3","Notebook", 15, 1500, "Positivo Tecnologia", "01/01/2024")

produto4 = protudo_novo("4","Mouse Gamer", 57,200,"Hyperx Gaming", "22/12/2023")

produtos_novos = [produto1, produto2, produto3,produto4]

for produto_novo in produtos_novos:
    produto_novo.print_produtos_novos()

