class exibir_produtos_do_estoque:
    def exibir_produtos_do_estoque():
        import estoque

class exibir_produtos_novos_do_estoque:
    def exibir_produtos_novos_do_estoque():
        import produtos_novos

class lojinha:
    print("\n************************************")
    print("***Bem-Vindo(a) à nossa lojinha!!***")
    print("************************************")
    print("\n////////////////////////////////////////////////////////////////////")
    print("///Esses são os produtos que constam no nosso estoque atualmente///")
    print("///////////////////////////////////////////////////////////////////")
    exibir_produtos_do_estoque.exibir_produtos_do_estoque()
    print("\n//////////////////////////////////////////////////////////////////")
    print("///Esses são os produtos novos que estão para chegar no estoque///")
    print("//////////////////////////////////////////////////////////////////")
    exibir_produtos_novos_do_estoque.exibir_produtos_novos_do_estoque()

