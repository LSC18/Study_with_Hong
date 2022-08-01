import sys
N = int(sys.stdin.readline())
deque = []
for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push_front':
        deque.insert(0,order[1])
    if order[0] == 'push_back':
        deque.append(order[1])
    if order[0] == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
            deque.remove(deque[0])
    if order[0] == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    if order[0] == 'front':
        if len(deque) == 0:
            print('-1')
        else:
            print(deque[0])
    if order[0] == 'back':
        if len(deque) == 0:
            print('-1')
        else:
            print(deque[-1])
    if order[0] == 'empty':
        if len(deque) == 0:
            print('1')
        else:
            print('0')
    if order[0] == 'size':
        print(len(deque))