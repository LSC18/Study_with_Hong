from collections import deque
import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
dvisit = [0]*(N+1)
bvisit = [0]*(N+1)

for _ in range(M):
    a,b = map(int,input().split())
    # graph[a].append(b)
    graph[a][b] = 1
    # graph[b].append(a)
    graph[b][a] = 1

def dfs(x):
    dvisit[x] = 1
    print(x, end=" ")
    # for i in graph[x]:
    for i in range(1, N + 1):
        if dvisit[i] == 0 and graph[x][i] == 1:
            dfs(i)

def bfs(x):
    q = deque([x])
    bvisit[x] = 1
    while q:
        out = q.popleft()
        print(out, end=" ")
        # for i in graph[x]:
        for i in range(1, N + 1):
            if bvisit[i] == 0 and graph[out][i] == 1:
                q.append(i)
                bvisit[i] = 1

dfs(K)
print()
bfs(K)