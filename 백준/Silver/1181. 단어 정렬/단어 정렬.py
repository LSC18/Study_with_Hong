N = int(input())
abc_len = []
for i in range(N):
    abc_len.append(input())
sort_abc = list(set(abc_len))
set_abc = []
for j in sort_abc:
    set_abc.append((len(j),j))
result = sorted(set_abc)
for _ in range(len(set_abc)):
    print(result[_][1])