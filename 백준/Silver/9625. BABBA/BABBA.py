k = int(input())
dp = [[0,0] for i in range(46)]
dp[0][0] = 1
for i in range(1,k+1):
    dp[i][0] = dp[i-1][1] # 전 B 값 -> 현 A 값
    dp[i][1] = dp[i-1][0] + dp[i-1][1] # 전 A + B 값 -> 현 B 값
print(dp[k][0],dp[k][1])