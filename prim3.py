import heapq  # Biblioteca que fornece uma fila de prioridade (heap), usada para pegar o menor valor rapidamente

# Função que executa o algoritmo de Prim
def prim(grafo, inicio):
    visitado = set()      # Conjunto para guardar os vértices já visitados
    mst = []              # Lista onde vamos armazenar as arestas da árvore geradora mínima
    custo_total = 0       # Variável para guardar o custo total da árvore
    arestas = [(0, inicio, None)]  # Começamos com o vértice inicial e peso 0. None é porque ainda não há origem.

    while arestas:
        # Retira do heap a aresta com menor peso
        peso, destino, origem = heapq.heappop(arestas)

        # Se ainda não visitamos esse vértice
        if destino not in visitado:
            visitado.add(destino)  # Marcamos como visitado

            # Se não for o primeiro vértice, adicionamos a aresta à árvore
            if origem is not None:
                mst.append((origem, destino, peso))
                custo_total += peso

            # Adiciona ao heap as arestas que saem desse vértice e vão para vértices não visitados
            for vizinho, peso_vizinho in grafo[destino]:
                if vizinho not in visitado:
                    heapq.heappush(arestas, (peso_vizinho, vizinho, destino))

    return mst, custo_total  # Retorna a árvore geradora mínima e seu custo total

# Função principal com grafo fixo
def main():
    # Grafo de exemplo (não direcionado) com tamanho intermediário
    grafo = {
        'A': [('B', 3), ('D', 1)],
        'B': [('A', 3), ('C', 5), ('E', 4)],
        'C': [('B', 5), ('F', 7)],
        'D': [('A', 1), ('E', 2), ('G', 8)],
        'E': [('B', 4), ('D', 2), ('F', 6), ('H', 9)],
        'F': [('C', 7), ('E', 6), ('I', 3)],
        'G': [('D', 8), ('H', 4)],
        'H': [('E', 9), ('G', 4), ('I', 2)],
        'I': [('F', 3), ('H', 2)]
    }

    inicio = 'B'  # Vértice inicial definido fixamente

    # Executa o algoritmo de Prim
    mst, custo = prim(grafo, inicio)

    # Mostra a árvore geradora mínima
    print("\nÁrvore Geradora Mínima:")
    for origem, destino, peso in mst:
        print(f"{origem} - {destino} (peso: {peso})")

    # Mostra o custo total da árvore
    print(f"Custo total: {custo}")

# Essa parte faz com que a função main só seja executada se rodarmos esse arquivo diretamente
if __name__ == "__main__":
    main()