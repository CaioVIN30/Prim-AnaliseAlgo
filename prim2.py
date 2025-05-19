import heapq  # Biblioteca para usar fila de prioridade (heap)

# Função que executa o algoritmo de Prim
def prim(grafo, inicio):
    visitado = set()      # Conjunto para guardar os vértices já visitados
    mst = []              # Lista das arestas da árvore geradora mínima (MST)
    custo_total = 0       # Soma dos pesos das arestas da MST

    # Fila de prioridade (min-heap), iniciando com o vértice inicial
    arestas = [(0, inicio, None)]  # (peso, destino, origem)

    while arestas:
        # Pega a aresta de menor peso
        peso, destino, origem = heapq.heappop(arestas)

        if destino not in visitado:
            visitado.add(destino)

            if origem is not None:
                mst.append((origem, destino, peso))
                custo_total += peso

            # Adiciona ao heap as arestas que saem desse vértice
            for vizinho, peso_vizinho in grafo[destino]:
                if vizinho not in visitado:
                    heapq.heappush(arestas, (peso_vizinho, vizinho, destino))

    return mst, custo_total

# =================== Grafo já definido ===================

# Grafo não direcionado representado como lista de adjacência
grafo = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

# Vértice inicial
inicio = 'A'

# Executa o algoritmo
mst, custo = prim(grafo, inicio)

# Exibe o resultado
print("Árvore Geradora Mínima:")
for origem, destino, peso in mst:
    print(f"{origem} - {destino} (peso: {peso})")

print(f"Custo total: {custo}")