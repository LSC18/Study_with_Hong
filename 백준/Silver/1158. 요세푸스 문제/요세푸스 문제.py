from collections import deque
n,m = map(int,input().split())
lst = deque(range(1,n+1))
ans = []
while len(lst) > 0:
    lst.rotate(-m+1)
    ans.append(str(lst.popleft()))
print('<'+', '.join(ans)+'>')