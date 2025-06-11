import matplotlib.pyplot as plt
import networkx as nx
import heapq

# Grafo de ejemplo (editable)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Dijkstra
def dijkstra(graph, start):
    print(f"Inicio en '{start}'")
    distances = {node: float('inf') for node in graph} # Inicializar distancias
    distances[start] = 0
    visited = set()
    queue = [(0, start)]

    while queue: # Mientras haya nodos por visitar
        dist, current = heapq.heappop(queue) # Extraer el nodo con la menor distancia
        if current in visited: # Si ya fue visitado, lo ignoramos
            continue
        visited.add(current) # Marcar como visitado
        print(f"Visito nodo '{current}' con distancia acumulada {dist}")
        for neighbor, weight in graph[current].items(): # Recorrer vecinos
            if neighbor not in visited: # Si el vecino no ha sido visitado
                new_dist = dist + weight
                if new_dist < distances[neighbor]: # Si la nueva distancia es menor que la conocida
                    distances[neighbor] = new_dist # Actualizar distancia
                    print(f" → Actualizo distancia de '{neighbor}' a {new_dist}")
                    heapq.heappush(queue, (new_dist, neighbor)) # Añadir a la cola de prioridad
    return distances

# Visualización simple del grafo y distancias
def draw_graph(graph, distances):
    G = nx.Graph()
    for node, edges in graph.items():
        for neighbor, weight in edges.items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=1000)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Mostrar las distancias calculadas
    for node, (x, y) in pos.items():
        plt.text(x, y - 0.1, f"Dist: {distances[node]}", ha='center', fontsize=8, color='blue')

    plt.title("Algoritmo de Dijkstra")
    plt.show()

# Ejecutar todo
inicio = 'A'
resultados = dijkstra(graph, inicio)
print("\nDistancias finales desde el nodo inicial:")
for nodo, distancia in resultados.items():
    print(f" - {nodo}: {distancia}")
draw_graph(graph, resultados)