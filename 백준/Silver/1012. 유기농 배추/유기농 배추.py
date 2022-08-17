from collections import deque

dx = [-1,0,0,1]
dy = [0,-1,1,0]

T = int(input())

def bfs(x,y):
    que = deque([(x,y)])
    graph[x][y] = 0
    # que = ((1,0),(2,1))

    while que:
        x,y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > M-1 or ny < 0 or ny > N-1:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                que.append((nx,ny))

for i in range(T):
    M,N,K = map(int,input().split())
    graph = [[0]*N for _ in range(M)]
    cnt = 0
    
    for j in range(K):
        x1,y1 = map(int,input().split())
        graph[x1][y1] = 1

    for a in range(M):
        for b in range(N):
            if graph[a][b] == 1:
                bfs(a,b)
                cnt += 1

    print(cnt)