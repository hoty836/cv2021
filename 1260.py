import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
data = [[0]*(n+1) for _ in range(n+1)]

#입력받은 graph array로 만들기
for _ in range(m):
    x, y = map(int, input().split())
    data[x][y] = 1
    data[y][x] = 1


#DFS 구현
'''def dfs(graph, root):
    visited = []
    stack = [root]
    while stack :
        now = stack.pop()
        if now not in visited :
            visited.append(now)
            stack.extend(graph[now])
    return visited'''
visited = [False]*(n+1)
          
def dfs(now):
    visited[now] = True
    print(now, end=' ')
    for i in range(1, n+1):
        if data[now][i] == 1 and visited[i] is False:
            dfs(i)

#BFS 구현
'''def bfs(graph, root):
    visited = []
    queue = [root]
    while queue :
        now = queue.pop(0)
        if now not in visited :
            visited.append(now)
            queue.extend(graph[now])
    return visited'''


def bfs(now):
    visited = [False]*(n+1)
    q = deque()
    q.append(now)
    visited[now] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in range(1, n+1):
            if data[now][i] == 1 and visited[i] is False:
                visited[i] = True
                q.append(i)


dfs(v)
print()
bfs(v)
print()
