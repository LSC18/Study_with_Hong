n,m = map(int,input().split())
nosee = []
nolisten = []
nono = []
for i in range(n):
    nosee.append(input())
for j in range(m):
    nolisten.append(input())
nosee = set(nosee)
nolisten = set(nolisten)
result = nosee & nolisten
result = sorted(list(result))
print(len(result))
for _ in result:
    print(_)