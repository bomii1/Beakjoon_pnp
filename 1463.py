N = int(input())

# BottomUp 방식
def makeOne(N):
    dp = [0] * (N+1)

    for i in range(2, N+1):
        dp[i] = dp[i-1] + 1

        if (i % 2 == 0):
            dp[i] = min(dp[i], 1 + dp[i//2])
        if (i % 3 == 0):
            dp[i] = min(dp[i], 1 + dp[i//3])
    return dp[N]

print(makeOne(N))


