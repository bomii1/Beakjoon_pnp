## 2775

#### Dynamic Programming

#### 간략한 문제 설명
- a층 b호에 사는 사람은 a-1층의 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야한다
- 아파트는 0층부터 있고, 각 층에는 1호부터 있으며, 0층의 i호에는 i명이 산다

#### 제한
- 1 <= k, n <= 14

각 층에는 최대 14호까지 있으므로 0층에는 14호까지의 값을 미리 넣어줌
```python
dp = [[0 for j in range(15)] for i in range(k+1)]
dp[0] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
```

#### 함수 apart(k, n)
- dp table은 각 테스트케이스를 돌릴 때마다 초기화 해주어야 값이 누적되지 않기 때문에 함수 안에 선언
- dp[i][j] = dp[i-1][j] + dp[i-1][j]
<img src="https://github.com/bomii1/Beakjoon_pnp/assets/101382369/bbec5c90-4cfe-40fa-b850-c2b1e624fb3b" width="650" height="350"> 

```python
def apart(k, n):
    dp = [[0 for j in range(15)] for i in range(k+1)]
    dp[0] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    for i in range(1, k+1):
        for j in range(1, n+1):
            if j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    return dp[k][n]
```

