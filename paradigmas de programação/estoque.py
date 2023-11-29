import produtos_lojinha

class produtos_estoque:
    def produtos_estoque():
        print("PRODUTO 1:")
        print("Nome:",produtos_lojinha.produto1.nome)
        print("quantidade:",produtos_lojinha.produto1.qtd)
        print("preço:",produtos_lojinha.produto1.preco)
        print("fornecedor:",produtos_lojinha.produto1.fornecedor)
        
        print("\nPRODUTO 2:")
        print("Nome:",produtos_lojinha.produto2.nome)
        print("quantidade:",produtos_lojinha.produto2.qtd)
        print("preço:",produtos_lojinha.produto2.preco)
        print("fornecedor:",produtos_lojinha.produto2.fornecedor)
        
        print("\nPRODUTO 3:")
        print("Nome:",produtos_lojinha.produto3.nome)
        print("quantidade:",produtos_lojinha.produto3.qtd)
        print("preço:",produtos_lojinha.produto3.preco)
        print("fornecedor:",produtos_lojinha.produto3.fornecedor)
        
        print("\nPRODUTO 4:")
        print("Nome:",produtos_lojinha.produto4.nome)
        print("quantidade:",produtos_lojinha.produto4.qtd)
        print("preço:",produtos_lojinha.produto4.preco)
        print("fornecedor:",produtos_lojinha.produto4.fornecedor)

class estoque:
    produtos_estoque.produtos_estoque()
