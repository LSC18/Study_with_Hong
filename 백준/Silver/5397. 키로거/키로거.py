n = int(input())
for i in range(n):
    stk = []
    tmp = []
    pwd = input()
    for j in pwd:
        if j == '<':
            if stk:
                tmp.append(stk.pop())
            continue
        elif j == '>':
            if tmp:
                stk.append(tmp.pop())
            continue
        elif j == '-':
            if stk:
                stk.pop()
            continue
        else:
            stk.append(j)
    tmp.reverse()
    stk += tmp
    print(''.join(stk))