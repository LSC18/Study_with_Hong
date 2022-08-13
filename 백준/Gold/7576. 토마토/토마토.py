from collections import deque
M,N = map(int,input().split())
graph = []
que = deque()
for _ in range(N):
    graph.append(list(map(int,input().split())))
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            que.append((i,j))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
    while que:
        x,y = que.popleft()
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if 0<=a<N and 0<=b<M and graph[a][b]==0:
                que.append([a,b])
                graph[a][b] = graph[x][y]+1
bfs()
answ = 0
for i in graph:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    answ = max(answ,max(i))
print(answ-1)