import java.util.List;

public class Main {

    public static void main(String[] args) {

        Grafo grafo = new Grafo(6);

        grafo.adicionarAresta(1, 6);
        grafo.adicionarAresta(2, 6);
        grafo.adicionarAresta(4, 3);
        grafo.adicionarAresta(5, 3);
        grafo.adicionarAresta(1, 3);
        grafo.adicionarAresta(1, 2);

        List<Integer> topSort = grafo.getTopologicalSort();

        System.out.println(topSort);
    }
}
