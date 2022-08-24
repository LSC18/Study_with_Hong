from collections import deque
N = int(input())
parent = deque(map(int,input().split()))
child = [[] for _ in range(N)]
super_parent = -1
for i in range(N):
    if parent[i] == -1:
        super_parent = i
        continue
    child[parent[i]].append(i)
exc = int(input())
# child[parent[exc]] <- exc

if parent[exc] == -1:
    print(0)
    exit(0)

child[parent[exc]].remove(exc)
parent[exc] = -1

# def dfs(now):
#     if child[now]:
#         result = 0
#         for i in child[now]:
#             result += dfs(i)
#         return result
#     else:
#         return 1
# print(dfs(0))

result = 0
def dfs(now):
    global result
    if len(child[now]) != 0:
        for i in child[now]:
            dfs(i)
    else:
        result += 1
dfs(super_parent)
print(result)