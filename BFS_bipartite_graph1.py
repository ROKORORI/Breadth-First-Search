import sys
from collections import deque
input = sys.stdin.readline


def bfs(start_node):
    global bipartite
    queue = deque([start_node])
    visit[start_node] = 2
    while queue:
        now_node = queue.popleft()
        for node in nodes[now_node]:
            if visit[node] == 0:
                if visit[now_node] == 2:
                    visit[node] = 3
                else:
                    visit[node] = 2
                queue.append(node)
            else:
                if visit[node] == visit[now_node]:
                    bipartite = 0


k = int(input().rstrip())
for _ in range(k):
    V, E = map(int, input().rstrip().split())
    nodes = [[] for i in range(V + 1)]
    for i in range(E):
        u, v = map(int, input().rstrip().split())
        nodes[u].append(v)
        nodes[v].append(u)

    visit, bipartite = [0] * (V + 1), 1
    for i in range(1, V + 1):
        if bipartite == 0:
            break
        if visit[i] == 0:
            bfs(i)
    print('YES' if bipartite else 'NO')