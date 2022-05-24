import java.util.ArrayList;
import java.util.List;

public class Principal {

    private static int board_size;

    public static List<Integer> resolverRainhas(int n) {
        board_size = n;
        List<Integer> config = new ArrayList<>();
        if (backtrack(config)) {
            return config;
        }
        return null;
    }

    /**
     *
     * @param config uma lista, onde a j-ésima posição indica
     *               a coluna ocupada pela rainha da j-ésima
     *               linha
     */
    private static boolean backtrack(
            List<Integer> config) {

        // visitar o vértice corrente: no caso,
        // apenas verificar se é uma config final
        if (config.size() == board_size) {
            return true;
        }

        // minha config é parcial, vou tentar esticá-la...
        for (int coluna = 0; coluna < board_size; coluna++) {
            if (!passoValido(config, coluna)) {
                continue;
            }

            // modifica a configuração corrente
            config.add(coluna);

            if (backtrack(config)) {
                return true;
            }

            // desfaz a última modificação
            config.remove(config.size() - 1);
        }

        return false;
    }

    private static boolean passoValido(
            List<Integer> config, int colunaCandidata) {

        // tem alguém na mesma coluna?
        if (config.contains(colunaCandidata)) {
            return false;
        }

        // tem alguém nas diagonais, acima da posição desejada?
        int linhaAlvo = config.size();
        for (int i = 1; i <= linhaAlvo; i++) {
            int colEsq = colunaCandidata - i;
            int colDir = colunaCandidata + i;
            int linha = linhaAlvo - i;

            if (config.get(linha) == colEsq) {
                return false;
            }

            if (config.get(linha) == colDir) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        List<Integer> result = resolverRainhas(2);
        System.out.println(result);
    }
}
