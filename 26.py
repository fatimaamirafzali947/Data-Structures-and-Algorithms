def rec_DFS (graph, start, visited=None):
    if visited is None:
        visited=[]
    visited.add(start)
    for ne in graph [start]:
        if ne not in visited:
            rec_DFS(graph, ne, visited)
    return visited