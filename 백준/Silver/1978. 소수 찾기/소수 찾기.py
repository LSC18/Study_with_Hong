N = int(input())
lst = map(int,input().split())
cnt = 0
for i in lst:
    noprime = 0
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                noprime += 1
        if noprime == 0:
            cnt += 1
print(cnt)