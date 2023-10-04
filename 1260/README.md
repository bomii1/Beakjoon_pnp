## 1260

#### DFS (Depth-First Search, 깊이우선탐색)
#### BFS (BFS, Breadth-First Search, 너비우선탐색)

입력 값을 토대로 인접 행렬로 변환

```python
N, M, V = map(int, input().split())

matrix = [[0 for j in range(N+1)] for i in range(N+1)]
visitedD = [0] * (N+1)
visitedB = [0] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1
```


