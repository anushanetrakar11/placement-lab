def criticalConnections(n, connections):
    graph = [[] for _ in range(n)]
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    disc = [-1] * n
    low = [-1] * n
    time = 0
    bridges = []

    def dfs(u, parent):
        nonlocal time
        disc[u] = low[u] = time
        time += 1

        for v in graph[u]:
            if v == parent:
                continue

            if disc[v] == -1:
                dfs(v, u)
                low[u] = min(low[u], low[v])

                if low[v] > disc[u]:
                    bridges.append([u, v])
            else:
                low[u] = min(low[u], disc[v])

    dfs(0, -1)
    return bridges


# -------- TEST --------
if __name__ == "__main__":
    n = 5
    connections = [[0,1],[1,2],[2,0],[1,3],[3,4]]
    print(criticalConnections(n, connections))
