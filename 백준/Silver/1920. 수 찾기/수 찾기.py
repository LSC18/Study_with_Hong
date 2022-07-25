# 시간초과 solution

# N = int(input())
# own = list(map(int,input().split()))
# m = int(input())
# pls = list(map(int,input().split()))
# stk = []
# for i in pls:
#     if i in own:
#         stk.append('1')
#     else:
#         stk.append('0')
# for j in range(N):
#     print(stk[j])

# N = int(input())
# own = list(map(int,input().split()))
# m = int(input())
# pls = list(map(int,input().split()))
# stk = []
# cnt = 0
# for i in pls:
#     for k in own:
#         if i == k:
#             cnt += 1
#     if cnt == 1:
#         stk.append('1')
#         cnt = 0
#     else:
#         stk.append('0')
#         cnt = 0
# for j in range(N):
#     print(stk[j])

N = int(input())
A = set(map(int, input().split()))	# 탐색 시간을 줄이기 위해 set으로 받음
M = int(input())
arr = list(map(int, input().split()))
for num in arr:
    if num in A:
        print(1)
    else:
        print(0)