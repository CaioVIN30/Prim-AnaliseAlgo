# Algoritmo de Prim em Python sem usar heapq (fila de prioridade)

def prim(grafo, inicio):
    # Conjunto para armazenar os vértices já incluídos na árvore geradora mínima
    visitado = set()

    # Lista para armazenar as arestas da árvore geradora mínima
    mst = []

    # Custo total da árvore
    custo_total = 0

    # Começa a partir do vértice inicial
    visitado.add(inicio)

    # Enquanto nem todos os vértices tiverem sido visitados
    while len(visitado) < len(grafo):
        menor_aresta = None
        menor_peso = float('inf')

        # Percorre todos os vértices já visitados
        for u in visitado:
            # Percorre os vizinhos de cada vértice visitado
            for v, peso in grafo[u]:
                # Se o vizinho ainda não foi visitado e a aresta tem peso menor que o atual mínimo
                if v not in visitado and peso < menor_peso:
                    menor_peso = peso
                    menor_aresta = (u, v, peso)

        # Se encontrou uma nova aresta válida
        if menor_aresta:
            u, v, peso = menor_aresta

            # Adiciona o novo vértice à árvore
            visitado.add(v)

            # Adiciona a aresta à lista da árvore mínima
            mst.append((u, v, peso))

            # Soma o peso da aresta ao custo total
            custo_total += peso
        else:
            # Se não encontrou nenhuma aresta, o grafo pode não ser conexo
            break

    return mst, custo_total


# =================== Exemplo de uso ===================

# Representação do grafo como lista de adjacência
grafo = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

# Executa o algoritmo de Prim a partir do vértice 'A'
mst, custo = prim(grafo, 'A')

# Exibe a árvore geradora mínima
print("Arvore Geradora Minima:")
for origem, destino, peso in mst:
    print(f"{origem} - {destino} (peso: {peso})")

# Exibe o custo total da árvore
print(f"Custo total: {custo}")