class protudo_novo1:
    nome = "Melância"
    qtd = 33
    preco = 25
    fornecedor = "Hortifruti"

class produto_novo2:
    nome =  "Chocolate"
    qtd = 100
    preco = 5
    fornecedor = "Cacau Show"

class produto_novo3:
    nome = "Computador"
    qtd = 15
    preco = 1500
    fornecedor = "Positivo Tecnologia"

class produto_novo4:
    nome = "Mouse Gamer"
    qtd = 67
    preco = 200
    fornecedor = "Hyperx gaming"

class produtos_novos:
    def exibir_produtos_novos():
        print("PRODUTO 1:")
        print("Nome:",protudo_novo1.nome)
        print("quantidade:",protudo_novo1.qtd)
        print("preço:",protudo_novo1.preco)
        print("fornecedor:",protudo_novo1.fornecedor)
        
        print("\nPRODUTO 2:")
        print("Nome:",produto_novo2.nome)
        print("quantidade:",produto_novo2.qtd)
        print("preço:",produto_novo2.preco)
        print("fornecedor:",produto_novo2.fornecedor)
        
        print("\nPRODUTO 3:")
        print("Nome:",produto_novo3.nome)
        print("quantidade:",produto_novo3.qtd)
        print("preço:",produto_novo3.preco)
        print("fornecedor:",produto_novo3.fornecedor)
        
        print("\nPRODUTO 4:")
        print("Nome:",produto_novo4.nome)
        print("quantidade:",produto_novo4.qtd)
        print("preço:",produto_novo4.preco)
        print("fornecedor:",produto_novo4.fornecedor)
    exibir_produtos_novos()