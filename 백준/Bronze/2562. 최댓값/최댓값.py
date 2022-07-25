s = []
for i in range(9):
    s.append(int(input()))
print(max(s))
print(int(s.index(max(s)))+1)