import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Classe para grafos simples, não-direcionados.
 * Utiliza HashSets de vizinhos, para cada vértice.
 * Vértices são inteiros de 1 a n.
 */
public class Grafo {

    private List<Set<Integer>> vizinhosPorVertice;

    private int quantVertices;
    private int quantArestas;

    public Grafo(int n) {
        this.quantVertices = n;
        this.vizinhosPorVertice = new ArrayList<>(n + 1);

        this.vizinhosPorVertice.add(null);  // posição 0 ficará nula

        for (int i = 1; i <= n; i++) {
            this.vizinhosPorVertice.add(new HashSet<>());
        }

    }

    public void adicionarVertice() {

    }

    public boolean existeAresta(int v, int w) {
        return this.vizinhosPorVertice.get(v).contains(w);
    }

    public void adicionarAresta(int v, int w) {
        this.vizinhosPorVertice.get(v).add(w);
        this.vizinhosPorVertice.get(w).add(v);
        this.quantArestas++;
    }

    public void removerAresta(int v, int w) {
        this.vizinhosPorVertice.get(v).remove(w);
        this.vizinhosPorVertice.get(w).remove(v);
        this.quantArestas--;
    }

    public int obterGrau(int v) {
        return this.vizinhosPorVertice.get(v).size();
    }

    public int getQuantArestas() {
        return this.quantArestas;
    }
}
