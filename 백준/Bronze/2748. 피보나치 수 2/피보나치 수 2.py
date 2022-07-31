n = int(input())
dp = [0]*(n+1)
dp[1] = 1
m = 2
while n >= 2:
    dp[m] = dp[m-2] + dp[m-1]
    m += 1
    if m == n+1:
        break
print(dp[n])