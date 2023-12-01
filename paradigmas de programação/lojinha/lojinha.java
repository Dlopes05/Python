package lojinha;

class Lojinha {
    public static void main(String[] args) {
        System.out.println("\n************************************");
        System.out.println("***Bem-Vindo(a) à nossa lojinha!!***");
        System.out.println("************************************");
        System.out.println("\n////////////////////////////////////////////////////////////////////");
        System.out.println("///Esses são os produtos que constam no nosso estoque atualmente///");
        System.out.println("///////////////////////////////////////////////////////////////////");
        lojinha_produtos.ver_produtos();
        System.out.println("\n//////////////////////////////////////////////////////////////////");
        System.out.println("///Esses são os produtos novos que estão para chegar no estoque///");
        System.out.println("//////////////////////////////////////////////////////////////////");
        Lojinha_novos.ver_novos();
        
    }
}

