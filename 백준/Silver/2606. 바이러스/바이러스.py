N = int(input())
M = int(input())
graph = [[]*N for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0
visit = [0]*(N+1)
def dfs(start):
    global cnt
    visit[start] = 1
    for i in graph[start]:
        if visit[i] == 0:
            dfs(i)
            cnt += 1
dfs(1)
print(cnt)
