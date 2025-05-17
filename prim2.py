import heapq

def prim(grafo, inicio):
    visitado = set()         # Conjunto de vértices visitados
    mst = []                 # Lista de arestas da árvore geradora mínima
    custo_total = 0          # Soma dos pesos das arestas da MST

    # Fila de prioridade (min-heap): (peso, destino, origem)
    arestas = [(0, inicio, None)]  # Começa do vértice inicial

    while arestas:
        peso, destino, origem = heapq.heappop(arestas)

        if destino not in visitado:
            visitado.add(destino)

            if origem is not None:
                mst.append((origem, destino, peso))
                custo_total += peso

            # Adiciona todas as arestas do vértice recém-visitado ao heap
            for vizinho, peso_vizinho in grafo[destino]:
                if vizinho not in visitado:
                    heapq.heappush(arestas, (peso_vizinho, vizinho, destino))

    return mst, custo_total


# =================== Exemplo de uso ===================

grafo = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

mst, custo = prim(grafo, 'A')

print("Árvore Geradora Mínima:")
for origem, destino, peso in mst:
    print(f"{origem} - {destino} (peso: {peso})")

print(f"Custo total: {custo}")