n = int(input())
mem = input().split()
arr = []
cnt = 1
for i in mem:
    i = int(i)
    if i == 0:
        arr.append(str(cnt))
    else:
        arr.insert(len(arr) - i, str(cnt))
    cnt += 1

print(" ".join(arr))

# arr = [1, 2, 3]
# new mem = 4 (2를 뽑음)
# len(arr) - 2