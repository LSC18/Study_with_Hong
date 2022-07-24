n,m = map(int,input().split())
nosee = []
nolisten = []
nono = []
for i in range(n):
    nosee.append(input())
for j in range(m):
    nolisten.append(input())
nosee = set(nosee)
nolisten = set(nolisten)
result = nosee & nolisten
result = sorted(list(result))
print(len(result))
for _ in result:
    print(_)
    

# 밑에 코드 == 때려 넣는 삭으로 짠 코드인데 시간초과 뜸. 처음 짠게 잘 짠듯.

# n,m = map(int,input().split())
# ownli = []
# newli = []
# result = []
# for i in range(n):
#     ownli.append(input())
# for j in range(m):
#     ownli.append(input())
# for v in ownli:
#     if v in newli:
#         result.append(v)
#     else:
#         newli.append(v)
# result = sorted(result)
# print(len(result))
# for _ in result:
#     print(_)
