N = int(input())
books = {}
res = []
for _ in range(N):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1
ans = max(books.values())
for j in books:
    if ans == books[j]:
        res.append(j)
print(sorted(res)[0])