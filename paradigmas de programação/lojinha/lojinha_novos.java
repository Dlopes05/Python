package lojinha;

import java.util.ArrayList;
import java.util.List;

    class ProdutoNovo {
    private String produto;
    private String nome;
    private int quantidade;
    private double preco;
    private String fornecedor;
    private String prazo;

    public ProdutoNovo(String produto, String nome, int quantidade, double preco, String fornecedor, String prazo) {
        this.produto = produto;
        this.nome = nome;
        this.quantidade = quantidade;
        this.preco = preco;
        this.fornecedor = fornecedor;
        this.prazo = prazo;
    }

    public void printProdutoNovo() {
        System.out.println("PRODUTO: " + this.produto);
        System.out.println("Nome: " + this.nome);
        System.out.println("Quantidade: " + this.quantidade);
        System.out.println("Preço: " + this.preco);
        System.out.println("Fornecedor: " + this.fornecedor);
        System.out.println("Prazo: " + this.prazo);
        System.out.println();
    }
}

    class Lojinha_novos {
    static void ver_novos() {
        List<ProdutoNovo> produtos = new ArrayList<>();

        produtos.add(new ProdutoNovo("1", "Melância", 33, 25, "Hortifruti", "10/12/2023"));
        produtos.add(new ProdutoNovo("2", "Chocolate", 100, 5, "Cacau Show", "03/12/2023"));
        produtos.add(new ProdutoNovo("3", "Computdor", 15, 1500, "Positivo Tecnologia", "01/01/2024"));
        produtos.add(new ProdutoNovo("4", "Mouse Gamer", 57, 200, "Hyperx Gamer", "22/12/2023"));

        for (ProdutoNovo ProdutoNovo : produtos) {
            ProdutoNovo.printProdutoNovo();
        }
    }
}
