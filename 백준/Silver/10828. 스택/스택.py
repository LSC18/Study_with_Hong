import sys
N = int(sys.stdin.readline())
stk = []
for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        stk.append(order[1])
    if order[0] == 'pop':
        if len(stk) == 0:
            print(-1)
        else:
            print(stk.pop())
    if order[0] == 'size':
        print(len(stk))
    if order[0] == 'empty':
        if len(stk) == 0:
            print(1)
        else:
            print(0)
    if order[0] == 'top':
        if len(stk) == 0:
            print(-1)
        else:
            print(stk[-1])