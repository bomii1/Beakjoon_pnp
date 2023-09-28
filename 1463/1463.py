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

"""
# TopDown 방식
def makeOne(N):
    #print("f(", N, ")")
    if N == 2 or N == 3:
        return 1
    if N == 1:
        return 0
    else:
        if N % 3 == 0:
            return min(makeOne(N-1) + 1, makeOne(N//3) + 1)
        elif N % 2 == 0:
            return min(makeOne(N-1) + 1, makeOne(N//2) + 1)
        else:
            return makeOne(N-1) + 1
"""