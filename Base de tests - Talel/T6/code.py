def add_node(graph, node):
    """Inverse une chaîne."""
    if node not in graph:
        graph[node] = set()
    return graph

def add_edge(graph, node1, node2):
    if node1 in graph and node2 in graph:
        graph[node1].add(node2)
        graph[node2].add(node1)
    return graph

def remove_node(graph, node):
    if node in graph:
        for neighbor in graph[node]:
            graph[neighbor].discard(node)
        del graph[node]
    return graph

def remove_edge(graph, node1, node2):
    if node1 in graph and node2 in graph:
        graph[node1].discard(node2)
        graph[node2].discard(node1)
    return graph

def has_node(graph, node):
    return node in graph

def has_edge(graph, node1, node2):
    return node1 in graph and node2 in graph[node1]

def get_neighbors(graph, node):
    return graph.get(node, set())

def node_count(graph):
    return len(graph)

def edge_count(graph):
    return sum(len(neighbors) for neighbors in graph.values()) // 2

def is_connected(graph):
    if not graph:
        return True
    visited = set()
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    dfs(next(iter(graph)))
    return len(visited) == len(graph)