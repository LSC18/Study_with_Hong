n,m = map(int,input().split())
if n > m:
    n,m = m,n
# n이 작은 수
# 최대공약수
mxval = 0
for num1 in range(1,n+1):
    if n % num1 == 0 and m % num1 == 0:
        mxval = num1
# 최소공배수
tmp = n//mxval
minval = tmp*m
print(mxval)
print(minval)