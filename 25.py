def bfs (graph, start):
    visited=set()
    queue=ins_queue([start])
    visited.add(start)
    tr_order=[]
    while queue:
        vartex=queue.pop()
        tr_order.append(vartex)
        for ne in graph[vartex]:
            if ne not in visited:
                visited.append(ne)
                queue.append(ne)
    return tr_order