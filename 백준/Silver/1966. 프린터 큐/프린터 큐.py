for _ in range(int(input())):
    N,M = map(int,input().split())
    a = list(map(int, input().split()))
    b = []
    for i in range(len(a)):
        b.append([a[i], i])
    a.sort(key = lambda x: -x)
    cnt = 0
    while True:
        num, idx = b.pop(0)
        if a[0] == num:
            cnt += 1
            a.pop(0)
            if idx == M:
                print(cnt)
                break
        else:
            b.append([num,idx])