N = int(input())
tmp = [0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(N):
    tmp[i] = int(input())
dp[0] = tmp[0]
dp[1] = tmp[0] + tmp[1]
dp[2] = max(tmp[1] + tmp[2], tmp[0] + tmp[2])
for i in range(3,N):
    dp[i] = max(dp[i-3] + tmp[i-1] + tmp[i], dp[i-2] + tmp[i])
print(dp[N-1])