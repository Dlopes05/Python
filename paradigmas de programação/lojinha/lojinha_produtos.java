package lojinha;

import java.util.ArrayList;
import java.util.List;

    class ProdutoEstoque {
    private String produto;
    private String nome;
    private int quantidade;
    private double preco;
    private String fornecedor;

    public ProdutoEstoque(String produto, String nome, int quantidade, double preco, String fornecedor) {
        this.produto = produto;
        this.nome = nome;
        this.quantidade = quantidade;
        this.preco = preco;
        this.fornecedor = fornecedor;
    }

    public void printProdutoEstoque() {
        System.out.println("PRODUTO: " + this.produto);
        System.out.println("Nome: " + this.nome);
        System.out.println("Quantidade: " + this.quantidade);
        System.out.println("Preço: " + this.preco);
        System.out.println("Fornecedor: " + this.fornecedor);
        System.out.println();
    }
}

    class lojinha_produtos {
    public static void ver_produtos(){
        List<ProdutoEstoque> produtos = new ArrayList<>();

        produtos.add(new ProdutoEstoque("1", "Maçã", 50, 20, "hortifruti"));
        produtos.add(new ProdutoEstoque("2", "Pasta de Dente", 20, 7, "drogasil"));
        produtos.add(new ProdutoEstoque("3", "Desodorante", 50, 11, "Old Spice"));
        produtos.add(new ProdutoEstoque("4", "Miojo", 100, 2, "Nissin"));

        for (ProdutoEstoque produtoEstoque : produtos) {
            produtoEstoque.printProdutoEstoque();
        }
    }
}

