def dp(k, n):
    dp = [[0 for j in range(15)] for i in range(k+1)]
    dp[0] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    for i in range(1, k+1):
        for j in range(1, n+1):
            if j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    return dp[k][n]

testCase = int(input())
res = []
for i in range(testCase):
    k = int(input())
    n = int(input())
    res.append(dp(k, n))

for i in range(testCase):
    print(res[i])

