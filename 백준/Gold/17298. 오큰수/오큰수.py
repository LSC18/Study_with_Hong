N = int(input())
A = list(map(int,input().split()))
s = []
answer = []

while len(A) > 0:
    tmp = A.pop()
    while len(s) > 0 and s[-1] <= tmp:
        s.pop()
    if len(s) == 0:
        answer.append(-1)
    else:
        answer.append(s[-1])
    s.append(tmp)

while len(answer) > 0:
    print(answer.pop(), end=" ")