# from collections import deque
# n,m = map(int,input().split())
# lst = deque(range(1,n+1))
# ans = []
# while len(lst) >= m:
#     lst.rotate(-m+1)
#     ans.append(str(lst.popleft()))
# for i in lst:
#     ans.append(str(i))
# print('<'+', '.join(ans)+'>')

from collections import deque
n,m = map(int,input().split())
lst = deque(range(1,n+1))
ans = []
while len(lst) > 0:
    for _ in range(m-1):
        lst.append(lst.popleft())
    ans.append(str(lst.popleft()))
print('<'+', '.join(ans)+'>')