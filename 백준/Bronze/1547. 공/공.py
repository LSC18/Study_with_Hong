N = int(input())
cup = [0,1,2,3]
for i in range(N):
    x, y = map(int, input().split())
    cup[x],cup[y] = cup[y],cup[x]
print(cup.index(1))