import sys
from collections import deque
input = sys.stdin.readline


def bfs_color(root, root_color):
    cnt = 0
    check = [0] + [1] * (n - 1)
    queue = deque([(root, root_color)])
    while queue:
        present_node, present_color = queue.popleft()
        cnt += price[present_node][present_color]
        for node in nodes[present_node]:
            if check[node] == 1:
                check[node] = 0
                if present_color == 0:
                    next_color = 1
                else:
                    next_color = 0
                queue.append((node, next_color))
    return cnt


#  0번 정점이 루트
n = int(input().rstrip())
nodes = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().rstrip().split())
    nodes[a].append(b)
price = [0] * n
for i in range(n):
    white, black = map(int, input().rstrip().split())
    price[i] = (white, black)
check_root = 0
min_price = min(bfs_color(0, 0), bfs_color(0, 1))
print(min_price)
