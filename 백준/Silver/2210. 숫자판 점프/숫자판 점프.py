from termios import N_TTY


def dfs(x,y,num):
    if len(num) == 6:
        if num not in result:
            result.append(num)
        return
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]

        if nx >= 0 and nx < 5 and ny >=0 and ny < 5:
            dfs(nx, ny, num + graph[nx][ny])
    
graph = []
result = []
for i in range(5):
    graph.append(list(map(str,input().split())))
for k in range(5):
    for l in range(5):
        dfs(k,l,graph[k][l])
print(len(result))